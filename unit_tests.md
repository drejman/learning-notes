# Guidelines for Writing Effective Unit Tests in NetBox Plugins

## What to unit test
"Tests shouldn’t verify units of code. Rather, they should verify units of behavior: 
something that is meaningful for the problem domain and, ideally, something that a business person can recognize as useful. 
The number of classes it takes to implement such a unit of behavior is irrelevant.
The unit could span across multiple classes or only one class, or even take up just a tiny method."[1](#References)

Tests should cover behaviors (**what** is expected to happen - returned result of calculations is correct, 
a record has been updated in the database etc.) and be decoupled from implementation (**how** is this achieved in code).
In other terms, tests should document the requirements and expectations about the solution, and as long as those are met,
you should have complete freedom of restructuring and refactoring of the underlying implementation.


### Test organization and file structure
Unit tests are written in pytest.
Tests should be placed next to the covered source files or modules. 
Test file should have ``_test.py`` suffix. Example structure:

```
custom_scripts/
  api/
    ServiceProvisioning/
      tests/
        InternetConnection_test.py
      InternetConnection.py
```


### Naming conventions
Test class names should follow `Test<TestedBehaviourScenarioOrModule>` naming. 
Test method names should reflect the behavior they are covering, i.e. `test_should_raise_validation_error_when_field_is_missing`
or `test_should_create_new_service_when_resources_are_found`.
Fixtures should be stored in the same test file. 
If they are used by multiple test files, they should be placed in the `conftest.py` file.

Calls inside test methods should be grouped in the _Arrange - Act - Assert_ subgroups.


### Test data preparation and test isolation
Use dynamic data whenever it's applicable. If object instantiation is complex, consider adding factories for that purpose. 

For code involving use of models and ORM, recommended approach is to use model bakery and testcontainers combination 
to produce actual records in local database over mocking database calls.  
However, it is still best to leverage the in-memory, intra-process communication and structure code in a way,
that as much as possible can be tested without any external dependencies (such as database).
Keep this in mind when implementing a solution 
(e.g. pushing side effects such as DB reads/writes to the beginning/end of processing).


### Faking, mocking and stubbing
Avoid excessive mocking. More than 2 mocks per test is excessive and signals either a poor design (tight coupling) 
or that chosen type of test is not fitting the scope of test (i.e. testing API request-response cycle at unit test level).

Prefer fake implementations you can write by hand and inject to the code being tested (i.e. by passing an argument
to the constructor) over using `unittest.mock.patch`


### Parametrization
Parametrize when you test the same behaviour with different data.
Do not parametrize when you are testing different behaviours with common setup - use a common setup function 
(e.g. a pytest fixture) instead.


## Examples and best practices

Example test file:

```python
from tested_module import PublicModuleApiClass


class TestedModuleTest:
    def test_module_functionality_should_produce_its_result(self):
        # Arrange:
        fake = FakeCollaborator()
        expected_data = get_expected_data()
        
        # Act:
        actual_data = PublicModuleApiClass(collaborator=fake).public_method()
        
        # Assert:
        assert expected_data == actual_data
```

Example of unit tests that involves models:

```python
class TestInternetConnectionServiceProvisioning:
    @pytest.mark.django_db  # decorator allowing test to use database
    def test_should_create_new_service_order_for_internet_connection(  # expected outcome described in test name
        self,
        tmf641_payload,
        network_port_dedicated_service,  # preconditions to the test moved to fixtures
        internet_subnet_wan_service,
    ):
        """
        Given provided UUIDs are not in use
        When creation of new Service Order is requested
        Then new Service Order in 'inProgress' state and with new id is created.
        """
        # arrange
        uuids = [str(uuid.uuid4()), str(uuid.uuid4()), str(uuid.uuid4())]
        service_order_item = tmf641_payload["serviceOrderItem"][0]

        # act
        result = ServiceOrderManager(
            payload=deepcopy(tmf641_payload),
            uuids=uuids,
            so_uuid=None,
            resources=None,
            candidate_config=None,
        ).createServiceOrder()

        # assert
        assert result["status"] == Constants.SUCCESS_STATUS

         # check ServiceOrder has been correctly created
        so = ServiceOrder.objects.get(uuid=uuids[0])  # get created ServiceOrder
        
        # validate key fields
        assert so.state == "inProgress"
        assert so.tmf641_payload["serviceOrderItem"][0]["service"]["id"] is not None
        
        # validate fields with data copied from payload were set
        assert so.description == tmf641_payload["description"]
        assert so.category == tmf641_payload["category"]
        assert so.external_id == tmf641_payload["externalId"]
        assert so.name == service_order_item["id"]
```


## Common pitfalls and anti-patterns

### Mocking django ORM
```python
class TestResourceDeleteEvent(SimpleTestCase):
    @patch("custom_scripts.api.Utils.TMF.Resource.objects.filter", resource_filter)
    @patch("custom_scripts.api.Utils.TMF.transaction.atomic", mock_transaction_atomic)
    @patch("custom_scripts.api.Utils.TMF.BearerConnection.objects.filter", bearer_filter)
    @patch("custom_scripts.api.Utils.TMF.Interface.objects.filter")
    @patch("dcim.models.Interface.save", save)
    @patch("resource_pools.models.adjacentprefixsid.AdjacentPrefixSid.delete", delete)
    @patch("resource_pools.models.physical_resource.BearerConnection.delete", delete)
    @patch("resource_pools.models.physical_resource.Resource.delete", delete)
    @patch("custom_scripts.api.Utils.TMF.AdjacentPrefixSid.objects.filter", adjsid_filter)
    def test_TMF639ResourceDeleteEvent(self, mock_interface_filter):
        mock_bundle_interface_queryset = MagicMock()
        mock_bundle_interface_queryset.exists.return_value = True
        mock_bundle_interface_queryset.first.return_value = bundleInterfaceObj()
        mock_interface_filter.return_value = mock_bundle_interface_queryset
        ...
```

While this approach may work, there are some drawbacks to consider:
- Mocking at this level can be time-consuming and prone to breaking, 
  as mocks must precisely match the structure and behavior of the ORM at the right locations.
- The performance gain from faster test execution is often minimal compared to the effort and fragility of maintaining these mocks.

An alternative approach is to restructure the code in a way that reduces dependencies on the ORM, making it easier to test. 
This not only simplifies testing but also improves the overall design of the code, leading to more maintainable and resilient solutions.


### Tests with no assertions
```python
class ProbeCreationTest(MockQueriesMixin, SimpleTestCase):
    def test_alarm_config_generation(self):
        data = {
            ...
        }
        results = ProbeCreation().update_alarm_configs(
            ProbeData(
                probe_name="paata02-node101-ams22-nl", site_z="USATLA008", neighbor_site="gblona039,sgsina007,nlsrka003"
            ),
            data,
            200,
            300,
        )

```

Tests should always `assert` some observable behavior - be it return value, side effect (like updating database),
some procedure call / message / event or combination of them.


### Merging together separate test cases
```python
@pytest.mark.parametrize(
    ("data", "action", "expected"),
    [
        (
            {"serviceOrderItem": [{"service": {"id": "0"}}]},
            "add",
            {"status": Constants.FAILURE_STATUS, "message": "Atleast one network-port-infra relation is required."},
        ),
        (
            {
                "serviceOrderItem": [
                    {
                        "service": {
                            "id": "1",
                            "serviceRelationship": [
                                {
                                    "id": "123",
                                    "relationshipType": "AttachTo",
                                    "service": {"@type": "network-port-infra"},
                                }
                            ],
                        }
                    }
                ]
            },
            "add",
            {"status": Constants.FAILURE_STATUS, "message": "Invalid Service ID : 123"},
        ),
        (
            {
                "serviceOrderItem": [
                    {
                        "service": {
                            "id": "2",
                            "serviceRelationship": [
                                {
                                    "id": "123",
                                    "relationshipType": "AttachTo",
                                    "service": {"@type": "network-port-infra"},
                                }
                            ],
                        }
                    }
                ]
            },
            "add",
            {"status": Constants.FAILURE_STATUS, "message": "CFS Service : 123, is not active"},
        ),
      ...
    ],
)
@patch("custom_scripts.api.ServiceProvisioning.ServiceOrderUtils.CustomService")
def test_validateServiceOrder(
    mock_CustomService: Mock,
    data: dict,
    action: str,
    expected: dict,
):
    service_id = data["serviceOrderItem"][0]["service"]["id"]

    match service_id:
        case "1":
            mock_CustomService.objects.get.side_effect = Exception()
        case "2":
            mock_CustomService.service_type = "CFS"
            mock_CustomService.state = Constants.SERVICE_STATE_INACTIVE
            mock_CustomService.objects.get.return_value = mock_CustomService
        case "3":
            mock_CustomService.service_type = "CFS"
            mock_CustomService.state = Constants.SERVICE_STATE_ACTIVE
            mock_CustomService.objects.get.return_value = mock_CustomService

    result = InfraConnection().validateServiceOrder(data, action)
    assert result == expected
```
A single test tries to cover too many scenarios, violating the single reason to fail and resulting in poor readability
and complex test logic. Here's a couple of hard-and-fast rules that should make you stop and think if the test shouldn't 
be broken down:
- can't give the test case precise name easily: `test_validateServiceOrder` name is not as descriptive as 
  `test_ServiceOrder_validation_should_fail_if_network_port_infra_relation_is_missing`
- test needs to include conditional logic (such as if-elseif-else, match-case or dictionary-dispatch statements)

Parametrization is great tool to cover more cases without repeating code, but should be used for testing the same
behavior with different data or preconditions, rather than squeezing separate scenarios into one test method.


## Coverage
Focus on the code worth testing, mainly "business logic" (conditional logic, control flow and data flow etc.).
Do not skip edge cases or error paths, but carefully consider whether it should tested as part of main flow
or have a dedicated test, possibly limiting the scope to the targeted error.


## References
1. "Unit Testing Principles, Practices and Patterns" Vladimir Khorikov

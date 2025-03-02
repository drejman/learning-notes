# Guidelines for writing good unit tests in Netbox

## Introduction
The fundamental task a Software Engineer performs is introducing a code change. 
Regardless of the type of the change (whether it's adding a feature, fixing a bug, improving the design or optimizing
resource usage) you will always face the same challenge - preserving existing behavior.[1]
Therefore, two main strategies to tackle this challenge emerge:
- **_Edit and Pray_**: this approach involves meticulously planning the changes, thoroughly understanding the code 
to be modified, and then implementing the changes. Once completed, the system is run to verify the change's success, 
followed by exploratory testing to ensure no unintended issues were introduced.
- **_Cover and Modify_**: this method emphasizes working with a safety net during software modifications. 
This "net" consists of comprehensive tests that encapsulate the code being changed. 
By surrounding the code with reliable tests, we can quickly assess the impact of changes — whether positive or negative. 
While careful planning and understanding remain essential, the feedback from tests enables more precise and confident adjustments.

The key difference enabling moving to second approach is **feedback**.[2]
Good automated tests suites are providing the fast feedback about changes just introduced. 
They reduce the cognitive load of having to know all the possible implications of your changes - good tests will tell
you whether your changes broke some functionality. 
Additionally, they have positive effect of reducing the fear of introducing changes.
Without tests, you will be incentivized to make the smallest possible changes just to finish your user story, which
over time leads to code rot, makes development harder and harder and results in decreased velocity.
With tests, you will have courage to improve the design iteratively, keeping the design fit for the functionality.


## General unit tests rules
Tests should follow FIRST principles:[3]
- **Fast**: Tests should run quickly.  
The faster they are, the more likely developers are to run them. The shorter the feedback loop, the better.
Write fast tests. Whole unit test suite shouldn't take more than 30 seconds so that you don't lose focus.
- **Independent**: Tests should not depend on other tests or external systems.  
It has to be possible to run any particular test in isolation, without running any other test before it.
Order of running the tests should not impact the results in any way and tests should be possible to run in parallel.
- **Repeatable**: Tests should always give exactly same result, no matter when (the first time or the millionth time) 
or where (locally, in container or on CI server) they are run.
- **Self-Validating**: Each test should have clear pass/fail criteria. Those are the only allowed results of the test,
with zero room for interpretation.
- **Timely**: Tests need to be written exactly when they are needed. If all signatures and interfaces are know,
the best time is just before writing implementation required to make it pass (TDD). The second-best time is just after
finishing a piece of code. Writing tests after the whole code is finished leads to fitting tests to code rather than
writing testable code.


## Writing Unit Tests
"Tests shouldn’t verify units of code. Rather, they should verify units of behavior: 
something that is meaningful for the problem domain and, ideally, something that a business person can recognize as useful. 
The number of classes it takes to implement such a unit of behavior is irrelevant.
The unit could span across multiple classes or only one class, or even take up just a tiny method." [4]



### Test organization and file structure
Unit tests are written in pytest.
Tests should be placed next to the covered source files. Test file should have ``_test.py`` suffix. Example structure:

```
custom_scripts/
  api/
    ServiceProvisioning/
      tests/
        InternetConnection_test.py
      InternetConnection.py
```


### Naming conventions
Test class names should follow `<TestedClass>Test` naming. Testing method should start with `test_<name_of_tested_method>`.
Fixtures should be stored in the same test file. If they are used by multiple test files, they should be placed in
the `conftest.py` file.

Calls inside test methods should be grouped in the _Arrange - Act - Assert_ subgroups.


### Test data preparation and test isolation
Use dynamic data whenever it's applicable.

For code involving use of models and ORM, recommended approach is to use model bakery and testcontainers combination 
to produce actual records in local database over mocking database calls.


### Faking, mocking and stubbing
Avoid excessive mocking. More than 2 mocks per test is excessive and signals either a poor design or that chosen type
of test is not fitting the scope of test (i.e. testing API request-response cycle at unit test level).

Prefer fake implementations you can write by hand and inject to the code being tested (i.e. by passing an argument
to the constructor) over using `unittest.mock.patch`


### Parametrization
Parametrize when you test the same behaviour with different data.
Do not parametrize when you are testing different behaviours with common setup - use a common setup function 
(e.g. a pytest fixture) instead.


## Examples and best practices

Example test file:

```python
from tested_module import CustomClass


class CustomClassTest:
    def test_my_method(self):
        # Arrange:
        fake = FakeCollaborator()
        expected_data = get_expected_data()
        
        # Act:
        actual_data = CustomClass(collaborator=fake).my_method()
        
        # Assert:
        assert expected_data == actual_data
```

Example of unit tests that involves models:

```python
@pytest.mark.django_db
class TestNetboxData:
    def test_get_asn(self, pe_device):
        """
        Get unique ASN of the network.
        """
        # Arrange:
        asn = random.randint(1, 65535)
        baker.make(models.BasebuildParameters, key="autonomous_system", value=asn)

        # Act:
        netbox_data = NetworkData(pe_device)
        actual_asn = netbox_data.get_asn()

        # Assert:
        assert actual_asn == asn
```


## Common pitfalls and anti-patterns

## Coverage
Focus on the code worth testing, mainly "business logic".
Do not skip edge cases or error paths.
As a rule of thumb, aim for 80% statements code coverage.


## References
1. Working Effectively with Legacy Code
2. Growing Object-Oriented Software, Guided by Tests
3. Clean Code
4. Unit Testing Principles, Practices and Patterns

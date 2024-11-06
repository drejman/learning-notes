## Part I: The Money Example

### Chapter 1. Multi-Currency Money
How to start writing tests, what to cover and what to keep on the list for later
- Made a list of the tests we knew we needed to have working
- Told a story with a snippet of code about how we wanted to view one operation
- Ignored the details of JUnit for the moment
- Made the test compile with stubs
- Made the test run by committing horrible sins
- Gradually generalized the working code, replacing constants with variables
- Added items to our to-do list rather than addressing them all at once

### Chapter 2. Degenerate Objects
How to translate a feeling about code into a test  
How to use Fake Implementation and Obvious Implementation
- Translated a design objection (side effects) into a test case that failed because of the objection
- Got the code to compile quickly with a stub implementation
- Made the test work by typing in what seemed to be the right code

### Chapter 3. Equality for All
How to use Value Objects  
How to use Triangulation Implementation strategy
- Noticed that our design pattern (Value Object) implied an operation
- Tested for that operation
- Implemented it simply
- Didn't refactor immediately, but instead tested further
- Refactored to capture the two cases at once

### Chapter 4. Privacy
Test using public interface (note however than if public method has bugs, it might affect result of the tests)  
Encapsulate the implementation details
- Used functionality just developed to improve a test
- Noticed that if two tests fail at once we're sunk
- Proceeded in spite of the risk
- Used new functionality in the object under test to reduce coupling between the tests and the code

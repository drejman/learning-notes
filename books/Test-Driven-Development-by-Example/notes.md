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

### Chapter 5. Franc-ly Speaking
Duplication and even copy-paste if fine (for now)
- Couldn't tackle a big test, so we invented a small test that represented progress
- Wrote the test by shamelessly duplicating and editing
- Even worse, made the test work by copying and editing model code wholesale
- Promised ourselves we wouldn't go home until the duplication was gone

### Chapter 6. Equality for All, Redux
Sometimes there is need to refactor and there are no tests in place - just create those tests before refactoring.  
Better safe than sorry.

- Stepwise moved common code from one class (`Dollar`) to a superclass (`Money`)
- Made a second class (Franc) a subclass also
- Reconciled two implementations — `equals()` — before eliminating the redundant one

### Chapter 7. Apples and Oranges
The implementation should reflect domain, not programming language concepts - but only after test requires it.

- Took an objection that was bothering us and turned it into a test
- Made the test run a reasonable, but not perfect way — `getClass()`
- Decided not to introduce more design until we had a better motivation

### Chapter 8. Makin' Objects
Tests are client code, they shouldn't be exposed to implementation details like subclasses, 
and rather test expected behaviours

- Took a step toward eliminating duplication by reconciling the signatures of two variants of the same method — `times()`
- Moved at least a declaration of the method to the common superclass
- Decoupled test code from the existence of concrete subclasses by introducing factory methods
- Noticed that when the subclasses disappear some tests will be redundant, but took no action

### Chapter 9. Times We're Livin' In
What to do if working on something we uncover something bad that yells to be fixed?
In practice if it's short just do it, but don't interrupt what's already an interruption.  

In TDD there's constant tuning of how big the steps are and that's totally fine.

- Were a little stuck on big design ideas, so we worked on something small we noticed earlier
- Reconciled the two constructors by moving the variation to the caller (the factory method)
- Interrupted a refactoring for a little twist, using the factory method in `times()`
- Repeated an analogous refactoring (doing to `Dollar` what we just did to `Franc`) in one big step
- Pushed up the identical constructors

### Chapter 10. Interesting Times
Good tests allow you to just run experiments instead of thinking and reasoning about the behaviour of the system.

- Reconciled two methods — `times()` — by first inlining the methods they called and then replacing constants with variables
- Wrote a `toString()` without a test just to help us debug
- Tried a change (returning `Money` instead of `Franc`) and let the tests tell us whether it worked
- Backed out an experiment and wrote another test. Making the test work made the experiment work

### Chapter 11. The Root of All Evil
It's really okay to remove tests when changing implementations, if there is no longer any reason to keep those tests.

- Finished gutting subclasses and deleted them
- Eliminated tests that made sense with the old code structure but were redundant with the new code structure

### Chapter 12. Addition, Finally
TDD doesn't guarantee good design or brilliant ideas - 
but it gives time and space for insight, and opportunity to apply it.

- Reduced a big test to a smaller test that represented progress ($5 + 10 CHF to $5 + $5)
- Thought carefully about the possible metaphors for our computation
- Rewrote our previous test based on our new metaphor
- Got the test to compile quickly
- Made it run
- Looked forward with a bit of trepidation to the refactoring necessary to make the implementation real

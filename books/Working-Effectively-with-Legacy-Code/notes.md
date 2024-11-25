## Part I: The Mechanics of Change

### Chapter 1. Changing Software
Four reasons to change software:
1. Adding a feature: changes structure and new functionality
2. Fixing a bug: changes structure and existing functionality
3. Improving the design (refactoring): changes structure
4. Optimizing resource usage: changes resource usage

Preserving existing behavior is one of the largest challenges in software development.
Even when we are changing primary features, we often have very large areas of behavior that we have to preserve.  

### Chapter 2. Working with Feedback
Two primary ways of making changes in the system:
- *Edit and Pray*: seems professional, but shows lack of deeper skills
- *Cover and Modify*: create a scaffolding or a vise that will keep in place everything that should not move
  (regression tests); assures that changes are introduced only in selected behaviours

There are many discussions about whether particular tests are unit tests. It might be helpful to focus on two qualities:
- Does the test run fast?
- Can it help us localize errors quickly?

Unit tests run fast. If they don’t run fast, they aren’t unit tests. Other kinds of tests often masquerade as unit tests. 
A test is not a unit test if:
1. It talks to a database.
2. It communicates across a network.
3. It touches the file system.
4. You have to do special things to your environment (such as editing configuration files) to run it.

Tests that do these things aren’t bad. Often they are worth writing, and you generally will write them 
in unit test harnesses. However, it is important to be able to separate them from true unit tests 
so that you can keep a set of tests that you can run fast whenever you make changes.

#### The Legacy Code Dilemma
> When we change code, we should have tests in place. To put tests in place, we often have to change code.

#### The Legacy Code Change Algorithm
When you have to make a change in a legacy code base, here is an algorithm you can use:
1. Identify change points.
2. Find test points.
3. Break dependencies.
4. Write tests.
5. Make changes and refactor.

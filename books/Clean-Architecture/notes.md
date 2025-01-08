## Part I Introduction

### Chapter 1. What Is Design and Architecture?
In every case, the best option is for the development organization to recognize and avoid its own overconfidence 
and to start taking the quality of its software architecture seriously.

To take software architecture seriously, you need to know what good software architecture is. 
To build a system with a design and an architecture that minimize effort and maximize productivity, 
you need to know which attributes of system architecture lead to that end.

That’s what this book is about. It describes what good clean architectures and designs look like, 
so that software developers can build systems that will have long profitable lifetimes.

### Chapter 2. A Tale of Two Values
Every software system provides two different values to the stakeholders: behavior and structure. 
Software developers are responsible for ensuring that both those values remain high. 
Unfortunately, they often focus on one to the exclusion of the other. Even more unfortunately, 
they often focus on the lesser of the two values, leaving the software system eventually valueless.

Software was invented to be “soft.” It was intended to be a way to easily change the behavior of machines. 
If we’d wanted the behavior of machines to be hard to change, we would have called it hardware.
To fulfill its purpose, software must be soft — that is, it must be easy to change.

If you give me a program that does not work but is easy to change, then I can
make it work, and keep it working as requirements change. Therefore the
program will remain continually useful.

### Chapter 3. Paradigm Overview
The three paradigms included in this overview are:
- **Structured programming** imposes discipline on direct transfer of control.
- **Object-oriented programming** imposes discipline on indirect transfer of control.
- **Functional programming** imposes discipline upon assignment.

### Chapter 4. Structured Programming
Dijkstra once said, “Testing shows the presence, not the absence, of bugs.” 
In other words, a program can be proven incorrect by a test, but it cannot be proven correct.

Structured programming forces us to recursively decompose a program into a set of small provable functions. 
We can then use tests to try to prove those small provable functions incorrect. 
If such tests fail to prove incorrectness, then we deem the functions to be correct enough for our purposes.

### Chapter 5. Object-Oriented Programming
Using an OO language makes polymorphism trivial. 
On this basis, we can conclude that OO imposes discipline on indirect transfer of control.

Dependency Inversion (DI) means that the source code dependency points in the opposite direction compared to the
flow of control. Its implications for the software architect are profound.
The fact that OO languages provide safe and convenient polymorphism means that any source code dependency,
no matter where it is, can be inverted.

What is OO? There are many opinions and many answers to this question. 
To the software architect, however, the answer is clear: OO is the ability, through the use of polymorphism, 
to gain absolute control over every source code dependency in the system. 
It allows the architect to create a plugin architecture, 
in which modules that contain high-level policies are independent of modules that contain low-level details. 
The low-level details are relegated to plugin modules that can be deployed and developed independently of the modules
that contain high-level policies.

### Chapter 6. Functional Programming
Variables in functional languages do not vary. All race conditions, deadlock conditions, and concurrent update
problems are due to mutable variables. You cannot have a race condition or a concurrent update problem 
if no variable is ever updated. You cannot have deadlocks without mutable locks.

In other words, all the problems that we face in concurrent applications — all the problems we face in applications 
that require multiple threads, and multiple processors — cannot happen if there are no mutable variables.

#### Event Sourcing
Event sourcing is a strategy wherein we store the transactions, but not the state.
When state is required, we simply apply all the transactions from the beginning of time.
More importantly, nothing ever gets deleted or updated from such a data store.
As a consequence, our applications are not CRUD; they are just CR. 
Also, because neither updates nor deletions occur in the data store, there cannot be any concurrent update issues.
If we have enough storage and enough processor power, we can make our applications entirely immutable — 
and, therefore, entirely functional.


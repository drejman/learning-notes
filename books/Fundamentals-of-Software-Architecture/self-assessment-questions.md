### Chapter 1: Introduction
1. *What are the four dimensions that define software architecture?*  
Software architecture consists of the structure of the system (foundations supporting the architecture), 
combined with architecture characteristics (“-ilities”) the system must support, architecture decisions, 
and finally design principles.<br><br>

2. What is the difference between an architecture decision and a design principle?
Architecture decisions define the rules for how a system should be constructed. A design principle
differs from an architecture decision in that a design principle is a guideline rather
than a hard-and-fast rule.<br><br>

3. *List the eight core expectations of a software architect.*  
Architect should:
    - Make architecture decisions
    - Continually analyze the architecture
    - Keep current with latest trends
    - Ensure compliance with decisions
    - Have diverse exposure and experience
    - Have business domain knowledge
    - Possess interpersonal skills
    - Understand and navigate politics<br><br>

4. *What is the First Law of Software Architecture?*  
"Everything in software architecture is a trade-off."  
Alternatively, it can be said that "If an architect thinks they have discovered something that isn’t a trade-off, more likely
they just haven’t identified the trade-off yet".<br><br>


### Chapter 2: Architectural Thinking
1. *Describe the traditional approach of architecture versus development and
explain why that approach no longer works.*  
(Short answer: traditional approach looks like waterfall: architect builds a set of artifacts, based on which development
is done, without any feedback loop, revisiting initial assumptions or next iterations. It is completely unfit to modern,
iterative methodologies for software development.)<br>  
Long answer:
Traditionally, an architect is responsible for things like analyzing business requirements to extract and define 
the architectural characteristics (“-ilities”), selecting which architecture patterns and styles
would fit the problem domain, and creating components (the building blocks of the system). 
The artifacts created from these activities are then handed off to the development team, 
which is responsible for creating class diagrams for each component, creating user interface screens, 
and developing and testing source code. It is the unidirectional arrow passing though the virtual and physical barriers 
separating the architect from the developer that causes all of the problems associated with architecture. 
Decisions an architect makes sometimes never make it to the development teams, and decisions development teams make that
change the architecture rarely get back to the architect. In this model the architect is disconnected 
from the development teams, and as such the architecture rarely provides what it was originally set out to do.<br><br>

2. *List the three levels of knowledge in the knowledge triangle and provide an
example of each.*  
The top and the smallest one is "what you know". Below that, there is bigger one "what you know you don't know".
The bottom and the biggest one is "what you don't know you don't know".<br><br>

3. *Why is it more important for an architect to focus on technical breadth rather
than technical depth?*  
Because architects must make decisions that match capabilities to technical constraints, a broad understanding
of a wide variety of solutions is valuable. Architects should focus on technical breadth so that they have a larger
quiver from which to draw arrows.  
(But they won't be actually firing those arrows themselves, so they don't need to know every nut and bolt.)<br><br>

4. *What are some of the ways of maintaining your technical depth and remaining
hands-on as an architect?*  
(Definitely not taking ownership of a code on a critical path for a project, which would require being both architect
and lead developer at the same time, probably leading not only to overtime and burnout, but also blocking progress
in at least one of those two areas. This is called bottleneck trap.)
There are several ways:
    - delegate the critical path and framework code to others on the development team and then
      focus on coding a piece of business functionality (a service or a screen) one to three
      iterations down the road
    - do frequent proof-of-concepts (POCs), but strive for production-quality code
    - tackle some of the technical debt stories or architecture stories, freeing the development team up 
      to work on the critical functional user stories
    - working on bug fixes within an iteration
    - automation by creating simple command-line tools and analyzers to help the development team 
      with their day-to-day tasks
    - do frequent code reviews
    - "practice coding from home"
    - (cool idea would be to have hackathons where roles are switched, e.g. architects and QAs code while
      developers architect and test)


### Chapter 3: Modularity
1. *What is meant by the term connascence?*  
"Two components are connascent if a change in one would require the other to be
modified in order to maintain the overall correctness of the system."  
Meilir Page-Jones<br><br>

2. *What is the difference between static and dynamic connascence?*  
Static connascence refers to source-code-level coupling, while dynamic connascence refers to execution-time
coupling.<br><br>

3. *What does connascence of type mean? Is it static or dynamic connascence?*  
CoT is a static connascence meaning that multiple components must agree on the type of an entity. 
Typically in statically typed languages this is checked at compile-time.  
In Python I think it's more a connascence of interface/protocol, which can be checked before runtime, 
but might also result in runtime errors.<br><br>

4. *What is the strongest form of connascence?*  
Strength of connascence is defined by the ease with which a developer can refactor that type of coupling.
Dynamic connascence is stronger than static connascence, and out of all types of dynamic connascence the strongest is
Connascence of Identity (CoI), which occurs when multiple components must reference the same entity.<br><br>

5. *What is the weakest form of connascence?*  
Connascence of Name (CoN) - multiple components must agree on the name of an entity.
Names of methods represents the most common way that code bases are coupled
and the most desirable, especially in light of modern refactoring tools that make
system-wide name changes trivial.<br><br>

6. *Which is preferred within a code base—static or dynamic connascence?*  
Static connascence is strongly preferred, as it is much easier to analyze call graph over  runtime calls.
Maybe with better tooling and observability this wouldn't be as much of an issue.


### Chapter 4: Architecture Characteristics Defined
1. *What three criteria must an attribute meet to be considered an architecture characteristic?*  
    - Specifies a non-domain design consideration
    - Influences some structural aspect of the design
    - Is critical or important to application success<br><br>

2. *What is the difference between an implicit characteristic and an explicit one?
Provide an example of each.*  
Implicit ones rarely appear in requirements, yet they’re necessary
for project success. For example, availability, reliability, and security underpin virtually all applications, 
yet they’re rarely specified in design documents. Explicit architecture characteristics appear in requirements
documents or other specific instructions.<br><br>

3. *Provide an example of an operational characteristic.*  
Availability, Continuity, Performance, Recoverability, Reliability/safety, Robustness, Scalability.<br><br>

4. *Provide an example of a structural characteristic.*  
Configurability, Extensibility, Installability, Leverageability/reuse, Localization, Maintainability, Portability,
Supportability, Upgradeability<br><br>

5. *Provide an example of a cross-cutting characteristic.*  
Accessibility, Archivability, Authentication (ensure users are who they say they are), 
Authorization (ensure users can access only certain functions withing the application), Legal, Privacy, Security,
Supportability, Usability/achievability<br><br>

6. *Which architecture characteristic is more important to strive for — availability or performance?*  
It depends ;) "never shoot for the best architecture, but rather *the least worst* architecture"<br><br>


### Chapter 5: Identifying Architecture Characteristics
1. *Give a reason why it is a good practice to limit the number of characteristics 
(“-ilities”) an architecture should support.*  
Each architecture characteristic the architecture support complicates the overall system design; supporting too many
leads to greater complexity before even starting to address the problem domain (the original problem motivation
for writing the software in the first place).<br><br>

2. *True or false: most architecture characteristics come from business requirements and user stories.*  
Most architecture characteristics come from listening to key domain stakeholders and collaborating with them
to determine what is important from a domain perspective. While this may seem like a straightforward activity,
the problem is that architects and domain stakeholders speak different languages.<br><br>

3. *If a business stakeholder states that time-to-market (i.e., getting new features and
bug fixes pushed out to users as fast as possible) is the most important business
concern, which architecture characteristics would the architecture need to support?*  
Agility, testability, deployability.<br><br>

4. *What is the difference between scalability and elasticity?*  
Scalability is the ability to handle a large number of concurrent users without serious performance degradation,
while elasticity is the ability to handle bursts of requests.<br><br>

5. *You find out that your company is about to undergo several major acquisitions to
significantly increase its customer base. Which architectural characteristics
should you be worried about?*  
Interoperability, scalability, adaptability, extensibility.<br><br>


### Chapter 6: Measuring and Governing Architecture Characteristics
1. *Why is cyclomatic complexity such an important metric to analyze for architecture?*
Architects and developers universally agree that overly complex code represents a code smell;
it harms virtually every one of the desirable characteristics of code bases: modularity, testability and so on.<br><br>

2. *What is an architecture fitness function? How can they be used to analyze an
architecture?*  
Any mechanism that provides an objective integrity assessment of some architecture characteristic 
or combination of architecture characteristics.<br><br>

3. *Provide an example of an architecture fitness function to measure the scalability
of an architecture.*  
(One possible fitness function would be a change of a performance metric (such as requests per second or throughput)
under load in comparison to baseline value divided by change of resources assigned.
Perfectly scalable system would get a value of 1.)<br><br>

4. *What is the most important criteria for an architecture characteristic to allow
architects and developers to create fitness functions?*  
Measurability, it needs to be possible to objectively measure.<br><br>


### Chapter 7: Scope of Architecture Characteristics
1. *What is an architectural quantum, and why is it important to architecture?*  
An independently deployable artifact with high functional cohesion and synchronous connascence,
i.e. part of the system (consisting of services, databases etc.) that can be deployed and removed on its own,
doing something purposeful (like a business capability or a workflow) synchronously coupled within this subsystem.<br><br> 

2. *Assume a system consisting of a single user interface with four independently
deployed services, each containing its own separate database. Would this system
have a single quantum or four quanta? Why?*  
Assuming that services are correctly split and each of them encompasses a separate bounded context,
system would have four quanta, due to deployment independence and separation.<br><br> 

3. *Assume a system with an administration portion managing static reference data
(such as the product catalog, and warehouse information) and a customer-facing portion managing the placement of orders. 
How many quanta should this system be and why?
If you envision multiple quanta, could the admin quantum and customer-facing quantum share a database?
If so, in which quantum would the database need to reside?*  
Preferred solution would be to have 2 quantas, as architecture characterics such as scalability and elasticity are
vastly higher for customer-facing portion than for administration side. Also static data might need to be optimized
for fast reads and searchability.  
However, if cost management is important characteristic then I would suggest having database in quantum with higher
requirements and performing separate update procedures from the second quantum.<br><br>


### Chapter 8: Component-Based Thinking
1. *We define the term component as a building block of an application — something the application does.
A component usually consist of a group of classes or source files.
How are components typically manifested within an application or service?*  
Simplest form of component is a library, which just wraps code at higher level of modularity then classes or objects.
Components also appear as subsystems, layers or services.<br><br>

2. *What is the difference between technical partitioning and domain partitioning?
Provide an example of each.*  
Technical partitioning means that on the top-level, functionality of the system is devided into technical capabilities:
presentation, business rules, services, persistence and so on (example is Model-View-Controller and variants).
In domain partitioning top-level division is around domains or workflows, for example e-commerce application
could be divided into CatalogCheckout, UpdateInventory, ShipToCustomer, Reporting, Analytics, UpdateAccounts.<br><br>

3. *What is the advantage of domain partitioning?*  
Each of the workflows is encapsulated within a single top-level component,
which better reflects the kinds of changes that most often occur in the projects.<br><br>

4. *Under what circumstances would technical partitioning be a better choice over domain partitioning?*  
It offers clear separation of technical concerns, which in turn creates useful levels of decoupling: change in one layer
might only affect neighbouring layers. This style of partitioning provides a decoupling technique, reducing rippling
side effects on dependent components. It also enables developers to find certain categories of the code 
in the code base quickly, as it is organized by capabilities, which is better where we have separate departments 
like Database Administration, Backend Development, Presentation etc.<br><br>

5. *What is the entity trap? Why is it not a good approach for component identification?*  
Is it as anti-pattern where components are structured around entities, while in real world database relationships
are typically a different thing than actual workflows in the application.  
Components created with the entity trap also tend to be too coarse-grained, offering no guidance whatsover
to the development team in terms of the packaging and overall structuring of the source code.<br><br>

6. *When might you choose the workflow approach over the Actor/Actions approach when identifying core components?*  
Actor/Actions approach fits well more traditional software development processes with significant upfront design,
where requirements feature distinct roles and the kinds of actions they can perform. Workflow approach suits better
teams using Agile software development.<br><br>

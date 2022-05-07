# Data Schemas
A data schema is a collection of well-defined tables and respective columns,
along with other properties such as primary keys, foreign keys constraints, 
data type, and predicates.

Typically, an application needs two data schemas: *input schema* and 
*output schema*. The application is then developed to consume data from the 
input schema and populate the output schema, which is also known as a
*solution schema*.

It's very important to keep in mind that we need to balance two conflicting 
goals when designing data schemas:
- Make the schema friendly to the end-user
- Make the schema computationally efficient

## Designing the input schema
The process of designing the input schema varies a lot from application to 
application. But there are two main ways to go about it as we discuss next.

### Starting from the solution
If we know what the client expects as an output of the solution, we can develop 
the application with that target in mind and the required input data becomes
a consequence of that design.

### Starting from the available data
If there is not much clarity about the expected output, an alternative is to 
start from the available data. In this case, we recommend starting with the 
least number of tables and columns possible and keep expanding as needed.

## Designing the output schema
The process of designing the output schemas is more straightforward 
compared with the input schema. Basically, we need to identify what the 
client expects to see as an output of the solution and design tables that 
achieve what they need.

In some cases, the client knows exactly what they need. For example, they 
might expect to feed the output from your solution directly into their IT 
system. In this case, they might tell you precisely what tables and columns 
they need.

In some other cases, the client is looking for dashboards that they can 
interact with. In this case, the goal is more toward designing an output 
schema that would facilitate dashboarding.

## Being Agile
The process of designing data schemas overlaps with the process of scoping 
the problem because when we think about the required input data and reports, 
we are forced to think about the requirements and end goals of the application. 

In fact, in a certain way, the data schemas establish agreements between 
developers and the client. You agree to develop the solution under the 
assumption that the data will have that structure and the client agrees that 
he will be able to provide and consume the data in that same structure.

But it's crucial to be flexible in this process. Both you and your client 
will likely change your minds several times throughout the development process.
Sometimes you will have compelling reasons to change the schema, sometimes 
your client will do. And that's fine. After all, we are adopters of the
Agile methodology. Hence, we understand that the solution will keep evolving 
over time, and so will its data schemas.

------------------------------------------------------------------------------
In the next section, you will start to prepare a development data instance 
and design the input schema of your application.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../1_data/README.md
[next]: ../3_development_instance/README.md
[help]: ../../0_help/README.md
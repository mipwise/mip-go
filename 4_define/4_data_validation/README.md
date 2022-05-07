# Data Validation
Bad data can easily yield wrong results even through well-written code. 
Therefore, to be reliable, a solution must be able to catch bad data before 
it reaches the solution engine. 

The best place to catch and handle bad data is right in the input schema. 
But to achieve that, in addition to primary keys, we need to establish 
relationships between tables via foreign key constraints, precisely define 
the data type of every column, and define additional data predicates when 
appropriate.

The key idea here is to be as precise as you can about what you expect the 
data to look like. This is opposed to guessing what can go wrong with the 
data and adding catches for each exception.

But how can we implement this in Python?

There is a fantastic Python package called [ticdat][ticdat_website] that 
automates most of the work for us and is fairly simple to use!
 
A lot more information about data validation and best practices can be
found in the [ticdat Wiki][ticdat_wiki] on GitHub.

[ticdat_website]: https://pypi.org/project/ticdat/
[ticdat_wiki]: https://github.com/ticdat/ticdat/wiki

In the *Develop* module, you will see how to implement data schemas using 
ticdat. But before that, there are a few more things that we need to review.

------------------------------------------------------------------------------
Click **Next** to learn about modeling.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../3_development_instance/README.md
[next]: ../5_modeling/README.md
[help]: ../../0_help/README.md
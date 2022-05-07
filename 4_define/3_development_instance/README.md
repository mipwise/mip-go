# Development Instance
Real-world data is almost always hard to deal with, from collection to 
cleansing to validation. But developers always need some sort of data for 
testing as they develop a solution. 

A big mistake is to start testing a solution with real-world (often large) 
data instances from the beginning. The outcome is quite obvious, we end up 
having to debug the data and the code at the same time, which can become 
quite messy and lead to a big waste of time.

A good practice is to start developing with a very small instance of the 
problem. The smaller, the better, as long as it's still representative of 
the problem being solved.

Next, we discuss two ways to obtain a small development instance.

## Generating synthetic data 
A very small instance can be crafted manually on a spreadsheet starting 
from the master data (for example, sites, time periods, and products). 
In this case, it’s a good idea to keep the notation simple and suggestive, 
such as `S1`, `S2` for sites, `P1`, `P2`, `P3` for products, and `1`, `2`, 
`3` for time periods. Quantitative data, such as demand and price, can be 
randomized or can be chunks copied from actual data, if available.

While this option might not necessarily be doable for some types of machine 
learning projects, it’s definitely a good option for optimization projects. 

In fact, except for performance, all aspects of an optimization application 
can be tested with small instances. In which case, even commercial solvers 
may be used for free (at occasion we wrote this, no license was required 
to use Gurobi to solve models with up to 2K variables and constraints for 
development purposes).

Another advantage of this option is that one can craft instances to stress 
and validate the code against situations that the client might face in the 
future but that are not present in the first datasets provided. Such 
instances are useful for writing unit testing, for example.

## Shrinking a real-world data-set
This can be done manually or via script. The goal is to simply restrict the 
whole data to a small subset by throwing away SKU, sites, time periods, or 
whatever makes sense to reduce the instance size.

This option usually yields larger instances compared to the synthetic data 
option. One big advantage of the shrinking method is that, if you can write 
a script to generate one instance, then you may be able to easily generate 
multiple instances.

## Next steps
In both cases, creating small development instances might take time, but 
it’s for sure a time worth spending. Besides the debugging time that it can 
save, this practice yields more reliable solutions because of the implied 
testing. In addition, small instances help us better understand the 
behavior of the solution, which then can result in performance improvement and 
innovation.

Therefore, we strongly encourage you to take some time now to create one 
small, representative data set for your problem. You might be surprised by how
insightful this exercise can be. But if you don't know where to start, it's 
a good opportunity to contact your Mip Mentor. He can walk you through some 
examples and help you to get started.

------------------------------------------------------------------------------
Once you are done, move to the next section to
learn about data validation.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../2_data_schemas/README.md
[next]: ../4_data_validation/README.md
[help]: ../../0_help/README.md
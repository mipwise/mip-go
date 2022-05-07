## Input schema
To implement a schema we simply create an instance of the `PanDatFactory`
class. 

Here is how we can create the input schema for the diet problem:
```python
from ticdat import PanDatFactory

input_schema = PanDatFactory(
    parameters=[['Parameter'], ['Value']],  
    foods=[['Food ID'], ['Food Name', 'Per Unit Cost']],
    nutrients=[['Nutrient ID'], ['Nutrient Name', 'Min Intake', 'Max Intake']],
    foods_nutrients=[['Food ID', 'Nutrient ID'], ['Quantity']])
```
The syntax is quite simple. We enter each table as a mapping of its name
to primary key fields (first list) and to data fields (second list). Here is
a generic example:

```python
table_name=[['Primary Key One', 'Primary Key Two', ...], ['Data Field One', 'Data Field Two', ...]]
```

Later, when we execute the program to load the data (from local files or 
from a database, for instance), it will look for these exact tables and 
these exact fields. If there is any mismatch, the program will through
an error. This is the first level of safety of our solution (safety as per tidy, 
tested, safe) because we can now implement solve engines confident that 
tables and fields' names will not be messed up.

### Parameters table
The `parameters` table is a default table that we use to store user
parameters, and there is nothing that we need to do about it at this time. 

------------------------------------------------------------------------------
Next, we will discuss some naming conventions.
### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../README.md
[next]: ../2_naming_conventions/README.md
[help]: ../../../0_help/README.md
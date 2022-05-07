## Row predicates
Row predicates add another layer of safety to our solution. The idea is to 
enforce rules that involve multiple fields. We will illustrate its usage 
with the `nutrients` table of the diet problem.

As the names suggest, **Min Intake** and **Max Intake** fields contain the 
minimum and maximum amount of each nutrient that the diet must provide. As 
such, anyone would expect that min intake is always less than or equal to 
max intake. Yet, as a developer, you must not assume that your client will 
only feed into your solution data that fulfill this requirement.

Perhaps you didn't even realize that min intake is greater than the max intake 
for carbohydrates in the sample `nutrients` table displayed in the [first 
subsection](../README.md).

To catch such dirty data, we can simply use the `add_data_row_predicate` 
method of the `PanDatFactory` class.

```python
from ticdat import PanDatFactory

input_schema = PanDatFactory(
    parameters=[['Parameter'], ['Value']],
    foods=[['Food ID'], ['Food Name', 'Per Unit Cost']],
    nutrients=[['Nutrient ID'], ['Nutrient Name', 'Min Intake', 'Max Intake']],
    foods_nutrients=[['Food ID', 'Nutrient ID'], ['Quantity']])

input_schema.add_data_row_predicate(table='nutrients', predicate_name='Min Intake <= Max Intake',
                                    predicate=lambda row: row['Min Intake'] <= row['Max Intake'])
```
As you can see, the input of the `predicate` argument is a function, a 
`lambda` function in this case, that will be executed on each row of the 
table and return a boolean, `True` or `False`.

------------------------------------------------------------------------------
Next, you will see how to add foreign key constraints to a data schema.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../3_data_types/README.md
[next]: ../5_foreign_key_constraints/README.md
[help]: ../../../0_help/README.md
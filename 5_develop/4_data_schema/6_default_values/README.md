## Default values
Sometimes, you or your client might want to test the app with a dataset that 
has some missing data to start with. For example, imagine you want to solve 
the diet problem, but you still don't have food costs. Knowing that the food 
cost can't be `NULL`, you might want to set the cost to be $1.00 for all 
foods and keep moving. Of course, you could set all the values to $1.00 
manually, but to make it more convenient, you can set a default value to the 
`Per Unit Cost` column. This way, when you upload to the app a `foods` table 
that has missing values in the `Per Unit Cost` column, it will
automatically get filled with that default value.

It's very simple to set default values. We only need to call the 
`set_default_value` method of `PanDatFactory`:

```python
from ticdat import PanDatFactory

input_schema = PanDatFactory(
    parameters=[['Parameter'], ['Value']],  
    foods=[['Food ID'], ['Food Name', 'Per Unit Cost']],
    nutrients=[['Nutrient ID'], ['Nutrient Name', 'Min Intake', 'Max Intake']],
    foods_nutrients=[['Food ID', 'Nutrient ID'], ['Quantity']])

input_schema.set_default_value(table='foods', field='Per Unit Cost', default_value=1.00)
```

------------------------------------------------------------------------------
Next, you will see how to define user parameters.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../5_foreign_key_constraints/README.md
[next]: ../7_user_parameters/README.md
[help]: ../../../0_help/README.md
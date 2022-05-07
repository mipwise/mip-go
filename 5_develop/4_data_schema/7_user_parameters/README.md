## User parameters
One of the most useful features of a purpose-built app is the parameters 
that allow business people to interact with the algorithms implemented 
behind the scenes.

For example, in the case of the diet problem, we may want to define a parameter 
to let users decide whether they want to ensure only whole portions of food 
or portions can be fractional.

We can add user parameters to the input schema (that's why we have the 
`parameters` table in there) by using the `add_parameter` method of 
`PanDatFactory`:
```python
from ticdat import PanDatFactory

input_schema = PanDatFactory(
    parameters=[['Parameter'], ['Value']],
    foods=[['Food ID'], ['Food Name', 'Per Unit Cost']],
    nutrients=[['Nutrient ID'], ['Nutrient Name', 'Min Intake', 'Max Intake']],
    foods_nutrients=[['Food ID', 'Nutrient ID'], ['Quantity']])

input_schema.add_parameter('Food Portions', default_value='Ensure whole portions', number_allowed=False,
                           strings_allowed=['Ensure whole portions', 'Portions can be fractional'])
```
Just like with data type, `add_parameter` has many arguments we can 
configure to precisely determine what type of values can be entered for the 
defined parameter. In the example of the **Food Portions** parameter above, 
the value must be a string and there are only two possible options: **Ensure 
whole portions** or **Portions can be fractional**.

On the app's interface, the 'Food Portions' parameter above will be 
displayed as a dropdown menu with the options listed in `strings_allowed`.

------------------------------------------------------------------------------
Next, you will see that we can create output schemas the same way we create 
input schemas.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../6_default_values/README.md
[next]: ../8_output_schema/README.md
[help]: ../../../0_help/README.md
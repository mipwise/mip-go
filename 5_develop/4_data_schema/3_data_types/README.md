## Data types
Now we implement another level of safety into your solution. This is the 
task that demands the most manual work in implementing a data schema, but 
it's also one of the biggest life-saver!

The goal is to avoid dirty data: a text where an integer was expected, a 
`NULL` where a date was expected, a negative number where a positive number 
was expected, etc. This list can be surprisingly long!

So, instead of leaving the possibilities open and guessing all that can go 
wrong, we adopt the approach of **defining exactly what we expect** and 
checking against that.

The good news is that ticdat provides a clean and easy way of doing that, 
which is using the `set_data_type` method of the `PanDatFactory` class.

### Example
Let's illustrate with the `foods` table:
```python
from ticdat import PanDatFactory

input_schema = PanDatFactory(
    parameters=[['Parameter'], ['Value']],
    foods=[['Food ID'], ['Food Name', 'Per Unit Cost']],
    nutrients=[['Nutrient ID'], ['Nutrient Name', 'Min Intake', 'Max Intake']],
    foods_nutrients=[['Food ID', 'Nutrient ID'], ['Quantity']])

input_schema.set_data_type(table='foods', field='Food ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table='foods', field='Food Name', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table='foods', field='Per Unit Cost', number_allowed=True, strings_allowed=(),
                           must_be_int=False, min=0.0, inclusive_min=True, max=float('inf'), inclusive_max=False)
```
You can probably figure out what's going on: we call the `set_data_type` 
method for each field and configure the arguments to specify exactly what we 
want. 

The fields **Food ID** and **Food Name**, for example, must be text. In 
addition, `strings_allowed='*'` says that it can be any text.

The field **Per Unit Cost** must be a number. In addition:
- `strings_allowed=()` says that it can't be a text;
- `must_be_int=False` says that it doesn't have to be an integer (whole number);
- `min=0.0, inclusive_min=True` says that the number must be greater than or
  equal to zero;
- `max=float('inf'), inclusive_max=False` says that the number must be 
  strictly less than infinity.

### Data type coverage
Basically, the `set_data_type` method allows us to assign each field to one 
of the following data type categories: text, numeric, or date. Then we can 
specify further details as shown next.

* **Text**
  - Any string  
    `number_allowed=False, strings_allowed='*'`
  - Only values from a given list of strings  
    `number_allowed=False, strings_allowed=['Breakfast', 'Lunch', 'Dinner']`
* **Numeric** (within a range, including or not each of the extremes)
  - Float  
    `number_allowed=True, strings_allowed=(), must_be_int=False,
     min=0.0, inclusive_min=True, max=1.0, inclusive_max=False`
  - Integer  
    `number_allowed=True, strings_allowed=(), must_be_int=True,
     min=0.0, inclusive_min=True, max=100, inclusive_max=True`
* **Date**
  - Datetime  
    `number_allowed=False, strings_allowed=(), datetime=True`

In addition, we can allow any field to contain `NULL` values by setting
`nullable = True`.

📝 **Tip:** *To learn more about an object in a code here in Pycharm,
press `CTRL` and then click on the object. It will take you to 
where the object is defined. So if the object is the method
`set_data_type`, for example, you will see its definition and 
its docstring documentation. This trick works even in code embedded 
in Markdown (not in the compiled view) like above!*

⚠️ **Warning** *We strongly recommend specifying the data type for
every field of every table of the schema (except for the 
`parameters` table). This allows developers to make
reliable assumptions about the data, which results in much safer 
programs.*

Not convinced about the warning above?  
Then check out this Jupyter Notebook: 
[Data Type Failure][data_type_failure]. Revisit the 
[Jupyter Notebook][jupyter_notebook] section if you need help to 
open and play with the notebook.

------------------------------------------------------------------------------
Next, you will learn how to add row predicates to a data schema.

[jupyter_notebook]: ../../../2_documentation/2_jupyter_notebook/README.md
[data_type_failure]: ../../../miscellaneous/notebooks/data_type_failures.ipynb

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../2_naming_conventions/README.md
[next]: ../4_row_predicates/README.md
[help]: ../../../0_help/README.md
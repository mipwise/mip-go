# Using Parameters
Let's have a look again at the implementation of the *Update Food Cost* action:
```python
def update_food_cost_solve(dat):
    """Increases food cost by 20%"""
    foods = dat.foods.copy()
    foods['Per Unit Cost'] = 1.2 * foods['Per Unit Cost']
    foods = foods.round({'Per Unit Cost': 2})
    dat.foods = foods[['Food ID', 'Food Name', 'Per Unit Cost']]
    return dat
```
It's a shame that this action can only increase the cost by 20%, and that's 
because the factor `1.2` is hard-coded. However, we can make this action 
much more useful by giving the end-user of our app a way to change this 
number, without having to access the code, of course!

To achieve that we can define a new user parameter in the input schema. We 
saw how to do this in the [User Parameters][user_parameters] section. In 
fact, we have already defined a parameter called *Food Cost Multiplier* in 
the sample [schemas.py][schemas] file, which is the file we are using in the 
`mip_me` package. In other words, the parameter Food Cost Multiplier is 
ready to be used.

Here is an updated version of the Update Food Cost action that shows how to 
use parameters:
```python
from mip_me import input_schema


def update_food_cost_solve(dat):
    """Multiply food cost by the Food Cost Multiplier parameter"""
    params = input_schema.create_full_parameters_dict(dat)
    foods = dat.foods.copy()
    foods['Per Unit Cost'] = params['Food Cost Multiplier'] * foods['Per Unit Cost']
    foods = foods.round({'Per Unit Cost': 2})
    dat.foods = foods
    return dat
```
All we did was replace `1.2` with `params['Food Cost Multiplier']`, where 
`params` is a dictionary that we always can get from the
`create_full_parameters_dict` method as above.

📝 **Tip:** 
*Parameters values can be stored in the `parameters` table. If that table is 
not available, or there is no record in there for the parameter you are 
trying to use, ticdat will use the default value defined in the input schema.*

[user_parameters]: ../4_data_schema/7_user_parameters/README.md
[schemas]: ../4_data_schema/9_sample_schemas/schemas.py

------------------------------------------------------------------------------
Next, you will see how to write data back to your local machine so that the 
changes made by an action can get saved.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../8_input_actions/README.md
[next]: ../10_writing_data/README.md
[help]: ../../0_help/README.md
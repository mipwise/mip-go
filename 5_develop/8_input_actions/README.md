# Input Actions
In this section, you will see how easy it is to implement an action engine 
and execute it locally.

We implement each action in a separate module whose name starts with the 
word `action`. This practice helps to keep the package organized and makes 
it easy to find an action code when the package has many scripts, even in 
someone else package.

To illustrate, we will create an action that updates the food cost of the 
diet problem. So, let's create (inside the package directory) a new file 
called `action_update_food_cost.py` to implement this action.

Here is the code that implements our *Update Food Cost* action:
```python
def update_food_cost_solve(dat):
    """Increases food cost by 20%"""
    foods = dat.foods.copy()
    foods['Per Unit Cost'] = 1.2 * foods['Per Unit Cost']
    foods = foods.round({'Per Unit Cost': 2})
    dat.foods = foods[['Food ID', 'Food Name', 'Per Unit Cost']]
    return dat
```
As you can see, the solve engine is just a Python function. Of course, for 
real-world problems, the script of an action may be much more complex than 
this, having multiple auxiliary functions or even importing other modules. 
But the logic will be the same.

Few more observations about the script above:
* Making a copy of the `foods` table is not required in this example.
  When tables are too large, for example, making a copy can consume
  excessive memory. On the other hand, this practice can prevent 
  unintended changes to the original data. So, it's a tradeoff to
  be considered.
* We're rounding the **Per Unit Cost** column to the second decimal
  place because high accuracy is not required in this example,
  and it will make the data easier to read on the app's interface. 
  Imagine how ugly it would be to display a number like `1.7999999999999998` 
  resulting from a multiplication like `1.2 * 1.5`.
* When we overwrite the `foods` table with the transformed dataframe,
  we list all the columns (a copy-and-paste from `schemas.py`) to
  improve the readability of the code and to make sure that what we are 
  writing back is what we expect. In fact, when performing a merge, 
  for instance, field names can get messed up. By listing the
  columns explicitly, we can catch such problems much more easily.

These little steps are examples of practices that can help to make the code 
significantly tidier and safer.

Now let's test our implementation by calling the action from the 
`execute_locally.py` script. To do so, replace it's current content with the 
following:
```python
from mip_me import input_schema
from mip_me.action_update_food_cost import update_food_cost_solve
path = "data/inputs"
dat = input_schema.csv.create_pan_dat(path)
print('Before:\n', dat.foods)
dat = update_food_cost_solve(dat)
print('After:\n', dat.foods)
```
The output will look like this:
```text
Before:
   Food ID   Food Name  Per Unit Cost
0      f1      Grapes            3.5
1      f2       Melon            5.6
2      f3  Watermelon            2.3
After:
   Food ID   Food Name  Per Unit Cost
0      f1      Grapes           4.20
1      f2       Melon           6.72
2      f3  Watermelon           2.76
```

Alternatively, we can import the action engine in the `__init__.py` and 
import it directly.
```python
__version__ = "0.1.0"
from mip_me.schemas import input_schema, output_schema
from mip_me.action_update_food_cost import update_food_cost_solve
```

```python
from mip_me import input_schema
from mip_me import update_food_cost_solve
path = "data/inputs"
dat = input_schema.csv.create_pan_dat(path)
print('Before:\n', dat.foods)
dat = update_food_cost_solve(dat)
print('After:\n', dat.foods)
```

------------------------------------------------------------------------------
Next, you will see how to improve the implementation of the input action 
above by using user parameters.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../7_solve_engines/README.md
[next]: ../9_using_parameters/README.md
[help]: ../../0_help/README.md
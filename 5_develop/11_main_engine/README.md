# Main Engines
Previously, we implemented and tested (by executing locally) an input action.
In this section, you will see that implementing and testing the main engine 
works the same way.

The main engine is dedicated to solving the core problem, which is the 
optimization problem in the case of the diet problem. And for 
standardization purposes, we implement the main engine (or call it from) a 
module called `main.py`. 

We already have a `main.py` in the `mip_me` package that was created 
automatically when we created the project. So let's go there and implement 
our solve code.

If you are not familiar with Python and optimization, the solving engine of 
`mip_me` might sound intimidating to you. But all you need to notice right 
now is that the solve function takes a `dat` object as an input, uses its 
data to do some stuff, and in the end it creates a `sln` object and 
populates the
`buy` table.

```python
from mip_me import output_schema

import pulp
import pandas as pd


def solve(dat):
    # Prepare optimization parameters
    I = set(dat.foods['Food ID'])
    J = set(dat.nutrients['Nutrient ID'])
    nl = dict(zip(dat.nutrients['Nutrient ID'], dat.nutrients['Min Intake']))
    nu = dict(zip(dat.nutrients['Nutrient ID'], dat.nutrients['Max Intake']))
    nq = dict(zip(zip(dat.foods_nutrients['Food ID'], dat.foods_nutrients['Nutrient ID']),
                  dat.foods_nutrients['Quantity']))
    c = dict(zip(dat.foods['Food ID'], dat.foods['Per Unit Cost']))

    # Build optimization model
    mdl = pulp.LpProblem("diet_problem", sense=pulp.LpMinimize)
    x = pulp.LpVariable.dicts(indexs=I, cat=pulp.LpContinuous, lowBound=0.0, name='x')
    for j in J:
        mdl.addConstraint(sum(nq[i, j] * x[i] for i in I) >= nl[j], name=f'nl_{j}')
        mdl.addConstraint(sum(nq[i, j] * x[i] for i in I) <= nu[j], name=f'nu_{j}')
    mdl.setObjective(sum(c[i] * x[i] for i in I))

    # Optimize and retrieve the solution
    mdl.solve()
    status = pulp.LpStatus[mdl.status]
    if status == 'Optimal':
        x_sol = [(key, var.value()) for key, var in x.items()]
    else:
        x_sol = None
        print(f'Model is not optimal. Status: {status}')

    # Populate output schema
    sln = output_schema.PanDat()
    if x_sol:
        x_df = pd.DataFrame(x_sol, columns=['Food ID', 'Quantity'])
        # populate buy table
        buy_df = x_df.merge(dat.foods[['Food ID', 'Food Name']], on='Food ID', how='left')
        buy_df = buy_df.round({'Quantity': 2})
        buy_df = buy_df.astype({'Food ID': str, 'Food Name': str, 'Quantity': 'Float64'})
        sln.buy = buy_df[['Food ID', 'Food Name', 'Quantity']]
    return sln

```
We will not discuss the details of this code at this time. But if you are in 
on optimization track, you will learn all the details of this script later.

To test the implementation of the main solve, let's first import it in 
`__init__.py`:
```python
__version__ = "0.1.0"
from mip_me.schemas import input_schema, output_schema
from mip_me.action_update_food_cost import update_food_cost_solve
from mip_me.main import solve
```
Next, go back to the `execute_locally.py` module and replace its current 
content with the following:
```python
from mip_me import input_schema, output_schema
from mip_me import solve

input_path = "data/inputs"
output_path = "data/outputs"
dat = input_schema.csv.create_pan_dat(input_path)
sln = solve(dat)
output_schema.csv.write_directory(sln, output_path)
```
Observe that we are reading CSV files from `inputs` and writing CSV files 
to `outputs`.

If the input data you're using is the development instance we introduced in 
the [Data Schema][data_schema] section, then you will not see the `buy` 
table being populated because the `nutrients` table has bad data: **Min 
Intake** is greater than **Max Intake** for Carbohydrates:

***nutrients***

| Nutrient ID |   Nutrient Name   | Min Intake | Max Intake |
|:-----------:|:-----------------:|:----------:|:----------:|
|     n1      |  Calories (kcal)  |   200.0    |   2000.0   |
|     n2      | Carbohydrates (g) | **250.0**  |   150.0    |

To fix it, set the **Min Intake** of Carbohydrates to be 50 instead of 250.

Executing `execute_locally.py` again after this adjustment should populate 
the `buy` table in the `outputs` directory. The `nutritions` table, however, 
will still be empty because it will be populated by an output action, which 
is your next step.

------------------------------------------------------------------------------
In the next section, you will learn to implement output actions.

[data_schema]: ../4_data_schema/README.md

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../10_writing_data/README.md
[next]: ../12_output_action/README.md
[help]: ../../0_help/README.md
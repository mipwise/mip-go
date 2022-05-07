# Output Action
In this section, we will implement and test an output action that will 
populate the `nutritions` table of our diet problem.

Let's create an action module named `action_report_builder.py` inside the 
script's directory and add the following content to it:
```python
def report_builder_solve(dat, sln):
    buy_df = sln.buy[['Food ID', 'Quantity']]
    nutrients_df = dat.nutrients[['Nutrient ID', 'Nutrient Name']]
    foods_nutrients_df = dat.foods_nutrients[['Food ID', 'Nutrient ID', 'Quantity']]
    foods_nutrients_df = foods_nutrients_df.rename(columns={'Quantity': 'Quantity per Food'})
    # merge buy and foods nutrients to get total nutrients of the diet
    nutrition_df = buy_df.merge(foods_nutrients_df, on='Food ID', how='left')
    nutrition_df['Quantity'] = nutrition_df['Quantity'] * nutrition_df['Quantity per Food']
    nutrition_df = nutrition_df[['Nutrient ID', 'Quantity']].groupby('Nutrient ID').agg('sum').reset_index()
    # merge nutrition with nutrients to get nutrient's names
    nutrition_df = nutrition_df.merge(nutrients_df, on='Nutrient ID', how='left')
    nutrition_df = nutrition_df.round({'Quantity': 2})
    nutrition_df = nutrition_df.astype({'Nutrient ID': str, 'Nutrient Name': str, 'Quantity': 'Float64'})
    sln.nutrition = nutrition_df[['Nutrient ID', 'Nutrient Name', 'Quantity']]
    return sln
```

Observe that the engine of this action takes to input arguments, a `dat` and 
a `sln` object because we need tables from both input and output schemas.

To test the implementation of this action, let's first import it in 
`__init__.py`:
```python
__version__ = "0.1.0"
from mip_me.schemas import input_schema, output_schema
from mip_me.action_update_food_cost import update_food_cost_solve
from mip_me.main import solve
from mip_me.action_report_builder import report_builder_solve
```

Next, update `execute_locally.py` as follows:
```python
from mip_me import input_schema, output_schema
from mip_me import report_builder_solve

input_path = "data/inputs"
output_path = "data/outputs"
dat = input_schema.csv.create_pan_dat(input_path)
sln = output_schema.csv.create_pan_dat(output_path)
sln = report_builder_solve(dat, sln)
output_schema.csv.write_directory(sln, output_path)
```
After execution, you should see the `nutrition` table populated.

------------------------------------------------------------------------------

With this, we have implemented the first version of our solution and tested 
all the engines with a development instance. Later, we will implement unit 
testing as well. But before that, we will get our package ready for 
deployment on Mip Hub, so we can start to play with it on the internet browser.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../11_main_engine/README.md
[next]: ../next_steps/README.md
[help]: ../../0_help/README.md
# Data Schema
We discussed how to define an input and output schema in Section [Data 
Schema][data_schema] of the module [Define][define]. Now it's time for you 
to implement the schemas you have defined!

We will be using [ticdat][ticdat], which is a Python package that will 
automate a lot of the hard work we would have to do in order to get our 
solution protected against dirty data. Not only that, but ticdat also helps 
end-users to identify and resolve issues in their data as we will see later. 
In addition, ticdat will help us to create and use parameters (that will
allow business people to interact with our solution), as well as organize 
and use data throughout the code. All of that will ultimately lead us to 
write tidy programs.

So before you continue, make sure to install the ticdat package on the 
Python interpreter that you are using in your project.

❔️ **Curiosity**  
*The name **ticdat** comes from the sentence "analytic data". Here, we 
explain how in a "Pythonic" way:* 🙃
```python
s1  = "analytic"
s2 = "data"
package_name = s1[-3:] + s2[:3]
```

## Diet Problem
We will use the Diet Problem to show you how to create schemas using ticdat.

Here is a statement of the problem:  
*Given a set of foods and a set of nutrients, the goal is to make a 
selection of food and the respective quantity to compose the least 
expensive diet that meets min and max recommended intake of nutrients.*

Here is a sample data, derived from our 
[development instance][development_instance] of the diet problem, with only 
three foods and two nutrients:

* ***foods***

| Food ID | Food Name  | Per Unit Cost |
|:-------:|:----------:|:-------------:|
|   f1    |   Grapes   |      3.5      |
|   f2    |   Melon    |      5.6      |
|   f3    | Watermelon |      2.3      |

* ***nutrients***

| Nutrient ID |   Nutrient Name   | Min Intake | Max Intake |
|:-----------:|:-----------------:|:----------:|:----------:|
|     n1      |  Calories (kcal)  |   200.0    |   2000.0   |
|     n2      | Carbohydrates (g) |   250.0    |   150.0    |

* ***foods_nutrients***

| Food ID | Nutrient ID | Quantity |
|:-------:|:-----------:|:--------:|
|   f1    |     n1      |   0.69   |
|   f2    |     n1      |   0.28   |
|   f3    |     n1      |   0.3    |
|   f1    |     n2      |  0.181   |
|   f2    |     n2      |  0.0658  |
|   f3    |     n2      |  0.0755  |

## Implementing the schema
In the future, you will most likely just copy a `schemas.py` file from 
another project and start overriding its content. But this time, we will 
create it from scratch.

### Creating the `schemas.py` file
Let's create a new script called `schemas.py`.

Right-click on the scripts' directory of your project (`mip_me` in our case),
go to `New > Python File`, then type in `schemas` and hit `Enter`.

📝 **Tip:** 
*If you need to rename a file in Pycharm, right-click on it and then choose 
`Refactor > Rename`.*

Now, go ahead and write the first line of code to import the `PanDatFactory` class:
```python
from ticdat import PanDatFactory
```
We will use this class to implement the input and output schema of our 
solution. More specifically, each schema will be an instance of this class.

If you're not familiar with classes, you can simply think of an instance of 
the `PanDatFactory` class as a collection of Pandas Dataframes, each table 
of the schema becomes a dataframe as you will see later. But if you would 
rather store tables as dictionaries, then you can use the `TicDatFactory` 
class instead. Defining schemas and performing all the tasks shown below work
the same way for both classes, only the way that data get stored will change.

------------------------------------------------------------------------------
Click **Next** once you be ready to continue.

[data_schema]: ../../4_define/2_data_schemas/README.md
[define]: ../../4_define/README.md
[ticdat]: https://github.com/ticdat/ticdat
[development_instance]: ../../4_define/3_development_instance/README.md

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../3_new_project/README.md
[next]: 1_input_schema/README.md
[help]: ../../0_help/README.md
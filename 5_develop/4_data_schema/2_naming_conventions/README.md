## Naming conventions
Next, we explain the naming conventions we adopt for fields and tables and 
the reasoning behind these choices.

Before you continue, we encourage you to stop for a minute and write down a 
few reasons why we should adopt and follow name conventions. If you 
don't know where to start, think of how name conventions can save us time 
and create consistency.

### Display names for fields
You may have noticed in the previous session that we're using **display 
names** for fields, i.e., the columns of each table are named as the 
end-user would expect to see them on the app. In fact, later when we deploy 
the app on Decision Station, these will be exactly the columns' names that 
we will see on the app's interface.

However, if you have a compelling reason to use back-end names for columns 
in your app (for example, the app is built in English and you want it to be 
displayed in another language), then you will see later how to overwrite 
columns' display names.

### Backend names for tables
Why don't we use display names for tables too? We can't do that because 
tables will become attributes of the `input_schema` object, and as an 
attribute, it must follow some 
[Python naming conventions][python_naming_conventions].
For example, later we can do `dat.foods_nutrients` to access the 
*foods_nutrients* table inside our code (where `dat` is an input schema 
populated with data), but `dat.Foods Nutrients` would through an error.

How are tables' names displayed on Mip Hub then?

The good news is that ticdat and Mip Hub will automatically convert 
`foods_nutrients` into **Foods Nutrients**, for example, before it gets 
displayed on the app's interface. In addition, we can overwrite this 
automatic conversion by specifying exactly what display name we want for 
any given table. For example, we might want the name of the table `bom` to be 
displayed as **Bill of Material** rather than **BOM**. We will see how to do 
this type of configuration later.

------------------------------------------------------------------------------
Next, you will see how to specify the data type for every field of a data 
schema.

[python_naming_conventions]: https://peps.python.org/pep-0008/#naming-conventions

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../1_input_schema/README.md
[next]: ../3_data_types/README.md
[help]: ../../../0_help/README.md
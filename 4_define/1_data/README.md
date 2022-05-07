# Data
If we are going to solve problems by combining data and algorithms, then 
knowing how to define and manipulate data is obviously a very important 
skill to develop. Data manipulation is a broad topic, so we will focus on 
the aspects that are most relevant to our context.

## Structures
The standard way to organize and store data is in the form of tables 
(though not always the most efficient way). Among the reasons for that is 
the fact that tables are human-readable.

In Python, tables are typically cast as Pandas data frames after the data is 
loaded from spreadsheets, CSV files, databases, etc. You will understand why 
is that once we start to learn more about Pandas later in the program.

To be used in the code, however, the data may have to be decomposed into 
other structures, such as lists, sets, tuples, or mappings/dictionaries.
For example, data frames are often suitable for descriptive analytics projects 
but lists and dictionaries are much easier to work with while building 
optimization models. Also, for more complex problems it may be a good idea 
to define classes and customized objects.

## Tables
Since we will be talking about tables quite a lot from now on, it's a good 
idea to introduce/review a few concepts about tables.

Tables have rows and columns. The first row is a special one which is 
called *header* and hosts the names of the columns. All the other rows host 
data.

Each column has a name and, ideally, holds data on one type only. For 
example, if you see that the first few entries of a column contain text, you 
would expect that the whole column contains only text. If that is not the 
case, you may have problems when you start using this data with your solution.

The following are two simple examples of tables.

**Table name: `sites`**

| Site ID |   Site Name    |  Latitude  | Longitude  |
|:-------:|:--------------:|:----------:|:----------:|
|   S0    |     Depot      | -27.600839 | -48.635966 |
|   S1    | Store Downtown | -27.596883 | -48.553225 |
|   S2    | Store Midtown  | -27.590798 | -48.504130 |

**Table name: `transit_matrix`**

| Origin Site ID | Dest. Site ID | Distance (KM) | Transit Time |
|:--------------:|:-------------:|:-------------:|:------------:|
|       S0       |      S1       |     25.4      |   0:46:00    |
|       S0       |      S2       |     32.2      |   1:06:00    |
|       S1       |      S0       |     23.0      |   0:32:00    |
|       S1       |      S2       |      8.8      |   0:16:00    |
|       S2       |      S0       |     31.7      |   0:32:00    |
|       S2       |      S1       |      8.9      |   0:17:00    |

There is probably nothing new for you until this point. What people are not 
so familiar with are the concepts of *primary keys* and *foreign keys* of a 
table.

### Primary keys
Primary keys are the values that uniquely identify its row. And all primary 
keys come from the same column or the same set of columns.

For example, in the `sites` table above, the **Site ID** column can be set 
as the *primary key* because its values, S0, S1, and S2, can be used to 
uniquely identify their respective rows. All the other columns in the 
`sites` table are then classified as *data columns*.

In the case of the `transit_matrix` table, we need two columns to define 
primary keys, they are **Origin Site ID** and **Dest. Site ID**.

### Foreign keys
The role of foreign keys is to establish relationships between tables.
Perhaps the most common example is foreign key constraints.

For example, it's probably a good idea to ensure that every
site ID that we encounter in the **Origin Site ID** and **Dest. Site ID**
columns is one of the primary keys of the `sites` table.
That way, if we want to retrieve the name or location of the sites
in the `transit_matrix` table, we can safely merge the two tables.

------------------------------------------------------------------------------
Next, we will discuss input and output data schemas.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../README.md
[next]: ../2_data_schemas/README.md
[help]: ../../0_help/README.md

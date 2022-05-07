## Foreign key constraints
As we saw in the [Data][data] section, foreign keys are useful to establish 
relationships between tables. Your code can easily break if you assume that 
two given tables are related when the actual data fails to fulfill that relationship.

For example, we would expect that any value that we encounter in the **Food 
ID** field of the `foods_nutrients` table is one of those values we 
encounter in the **Food ID** field of the `foods` table. A similar 
relationship should hold between `foods_nutrients` and `nutrients` tables.

To implement these two relationships using ticdat, we use the 
`add_foreign_key` method of the `PanDatFactory` class.

### Example 1: diet problem
The syntax is quite intuitive: we have to inform the name of the native 
table, the name of the foreign table, and a mapping between fields of the 
two tables.

In this example, each mapping is a pair of fields, native field and foreign 
field, respectively.
```python
from ticdat import PanDatFactory

input_schema = PanDatFactory(
    parameters=[['Parameter'], ['Value']],
    foods=[['Food ID'], ['Food Name', 'Per Unit Cost']],
    nutrients=[['Nutrient ID'], ['Nutrient Name', 'Min Intake', 'Max Intake']],
    foods_nutrients=[['Food ID', 'Nutrient ID'], ['Quantity']])

input_schema.add_foreign_key(native_table='foods_nutrients', foreign_table='foods',
                             mappings=('Food ID', 'Food ID'))
input_schema.add_foreign_key(native_table='foods_nutrients', foreign_table='nutrients',
                             mappings=('Nutrient ID', 'Nutrient ID'))
```
It's just a coincidence that in this example native field and foreign field 
have the same name. 

### Example 2: transportation data
Here is an example using another data schema where the native field and foreign 
field have different names:
```python
from ticdat import PanDatFactory

input_schema = PanDatFactory(
    parameters=[['Parameter'], ['Value']],
    sites=[['Site ID'], ['Site Name', 'Latitude', 'Longitude']],
    transit_matrix=[['Origin Site ID', 'Dest. Site ID'], ['Distance (KM)', 'Transit Time']])

input_schema.add_foreign_key(native_table='transit_matrix', foreign_table='sites',
                             mappings=('Origin Site ID', 'Site ID'))
input_schema.add_foreign_key(native_table='transit_matrix', foreign_table='sites',
                             mappings=('Dest. Site ID', 'Site ID'))
```

But how do we decide which table is the ``native_table`` (aka ``child table``) 
and which is the
``foreign_table`` (aka ``parent_table``)? As the child-parent names suggest, the `native_table` is the one
with fields that must match some other table, while the ``foreign_table`` contains the matching entries. In example 2,
``sites`` is the main (parent) table and `transit_matrix` is built from `sites` (child).

### Example 3: multiple mappings
Now suppose that we add a `paths` table to the schema of Example 2. For each 
value of **Path ID** in this table, we have a sequence of legs (arcs) that 
define a path. But we only want to allow legs whose **From** and **To** 
values match one of the **Origin Site ID** and **Dest Site ID** values in 
the `transit_matrix` table. To put it in another way, we want **From** to 
match **Origin Site ID** and **To** to match **Dest. Site ID**, concurrently.
```python
from ticdat import PanDatFactory

input_schema = PanDatFactory(
    parameters=[['Parameter'], ['Value']],
    sites=[['Site ID'], ['Site Name', 'Latitude', 'Longitude']],
    transit_matrix=[['Origin Site ID', 'Dest. Site ID'], ['Distance (KM)', 'Transit Time']],
    paths=[['Path ID', 'Leg Number'], ['From', 'To']])

input_schema.add_foreign_key(native_table='paths', foreign_table='transit_matrix',
                             mappings=[('From', 'Origin Site ID'), ('To', 'Dest. Site ID')])
```
So, in this case, `mappings` is a list of pairs of native and foreign 
fields rather than a single pair (as we saw in Example 1 and Example 2). 

[data]: ../../../4_define/1_data/README.md

------------------------------------------------------------------------------
Next, you will see how to set default values to fields.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../4_row_predicates/README.md
[next]: ../6_default_values/README.md
[help]: ../../../0_help/README.md
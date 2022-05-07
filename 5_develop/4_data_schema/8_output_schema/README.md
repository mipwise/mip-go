## Output schema
We can create the output schema in exact same way that we created the input 
schema. Here is an example:

```python
from ticdat import PanDatFactory

output_schema = PanDatFactory(
    buy=[['Food ID'], ['Food', 'Quantity']],
    nutrition=[['Nutrient ID'], ['Nutrient', 'Quantity']])
```

We can then set data types, row predicates, and foreign key constraints, 
just like we did in the input schema.

We don't add a `parameters` table to the output schema, though we 
technically could. We adopted the convention of always keeping  it in the 
input schema.

Another observation is that it's not possible to set foreign key 
constraints between tables of different schemas. In other words, both native 
and foreign tables must belong to the same schema, either inputs or outputs.

------------------------------------------------------------------------------
Next, you will see a complete `schemas.py` file that you can use as 
a reference for your future projects.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../7_user_parameters/README.md
[next]: ../9_sample_schemas/README.md
[help]: ../../../0_help/README.md
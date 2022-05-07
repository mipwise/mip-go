"""
Defines the input and output schemas of an adapted version of the diet problem.
"""

from ticdat import PanDatFactory

# region INPUT SCHEMA
input_schema = PanDatFactory(
    # syntax: table_name=[['Primary Key One', 'Primary Key Two'], ['Data Field One', 'Data Field Two']]
    parameters=[['Name'], ['Value']],
    foods=[['Food ID'], ['Food Name', 'Per Unit Cost']],
    nutrients=[['Nutrient ID'], ['Nutrient Name', 'Min Intake', 'Max Intake']],
    foods_nutrients=[['Food ID', 'Nutrient ID'], ['Food Name', 'Nutrient Name', 'Quantity']])
# endregion

# region USER PARAMETERS
input_schema.add_parameter('Food Portions', default_value='Ensure whole portions', number_allowed=False,
                           strings_allowed=['Ensure whole portions', 'Portions can be fractional'])
input_schema.add_parameter('Food Cost Multiplier', default_value=1.5, number_allowed=True, strings_allowed=(),
                           must_be_int=False, min=0.0, inclusive_min=True, max=10, inclusive_max=True)
# endregion

# region OUTPUT SCHEMA
output_schema = PanDatFactory(
    buy=[['Food ID'], ['Food Name', 'Quantity']],
    nutrition=[['Nutrient ID'], ['Nutrient Name', 'Quantity']])
# endregion

# region DATA TYPES AND PREDICATES - INPUT SCHEMA
# region foods
table = 'foods'
input_schema.set_data_type(table=table, field='Food ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Food Name', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Per Unit Cost', number_allowed=True, strings_allowed=(),
                           min=0, inclusive_min=True, max=float('inf'), inclusive_max=False)
input_schema.set_default_value(table=table, field='Per Unit Cost', default_value=1.00)
# endregion
# region nutrients
table = 'nutrients'
input_schema.set_data_type(table=table, field='Nutrient ID', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Nutrient Name', number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Min Intake', number_allowed=True, strings_allowed=(),
                           min=0, inclusive_min=True, max=float('inf'), inclusive_max=False, nullable=False)
input_schema.set_data_type(table=table, field='Max Intake', number_allowed=True, strings_allowed=(),
                           min=0, inclusive_min=True, max=float('inf'), inclusive_max=False, nullable=True)
input_schema.add_data_row_predicate(table=table, predicate_name='Min Intake <= Max Intake',
                                    predicate=lambda row: row['Min Intake'] <= row['Max Intake'])
# endregion
# region foods_nutrients
table = 'foods_nutrients'
for field in ['Food ID', 'Nutrient ID', 'Food Name', 'Nutrient Name']:
    input_schema.set_data_type(table=table, field=field, number_allowed=False, strings_allowed='*')
input_schema.set_data_type(table=table, field='Quantity', number_allowed=True, strings_allowed=(),
                           min=0, inclusive_min=True, max=float('inf'), inclusive_max=False)
input_schema.add_foreign_key(native_table=table, foreign_table='foods', mappings=[('Food ID', 'Food ID')])
input_schema.add_foreign_key(native_table=table, foreign_table='nutrients', mappings=[('Nutrient ID', 'Nutrient ID')])
# endregion
# endregion

# region DATA TYPES AND PREDICATES - OUTPUT SCHEMA
# region buy
table = 'buy'
output_schema.set_data_type(table=table, field='Food ID', number_allowed=False, strings_allowed='*')
output_schema.set_data_type(table=table, field='Food Name', number_allowed=False, strings_allowed='*')
output_schema.set_data_type(table=table, field='Quantity', number_allowed=True, strings_allowed=(),
                            min=0, inclusive_min=True, max=float('inf'), inclusive_max=False)
# endregion
# region nutrition
table = 'nutrition'
output_schema.set_data_type(table=table, field='Nutrient ID', number_allowed=False, strings_allowed='*')
output_schema.set_data_type(table=table, field='Nutrient Name', number_allowed=False, strings_allowed='*')
output_schema.set_data_type(table=table, field='Quantity', number_allowed=True, strings_allowed=(),
                            min=0, inclusive_min=True, max=float('inf'), inclusive_max=False)
# endregion
# endregion

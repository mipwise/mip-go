# Writing Data
Similar to what happens with loading there are many ways we can write data 
to a local directory. But we will be using ticdat again.

## Writing data as a collection of CSV files
The companion of the `csv.create_pan_dat` method that we saw in
the [Loading Data](../6_loading_data/README.md) session is 
`.csv.write_directory`.

To see how it works, go back to the `execute_locally.py` file and add the 
following line of code: 
`input_schema.csv.write_directory(dat, path)`.

Now, after executing `execute_locally.py`, you will see that the `foods.csv` 
file in the `inputs` directory will be modified as expected. 

⚠️ **Warning**  *Always make sure to keep a copy of your original input data 
in a place where it will not get messed up by actions executions.*

For convenience, you can implement a Data Ingestion action to pull a copy of 
the original data into the `inputs` directory. This would be equivalent to 
uploading a new dataset to your app on Mip Hub.

## Writing data as an Excel file
If you try to simply replace `csv` with `xls` in the previous code, you will 
get an error. Because with `xls` we are not writing to a directory, we are 
writing to a file instead. So the right command is this:
`input_schema.xls.write_file(dat, path)`.

However, this is still not enough! You need to include in the path the name 
of the worksheet you want to write to. So here is a script that will work 
for us:
```python
from mip_me import input_schema
from mip_me import update_food_cost_solve
input_path = "data/inputs"
output_path = "data/inputs/testing_data.xlsx"
dat = input_schema.csv.create_pan_dat(input_path)
dat = update_food_cost_solve(dat)
input_schema.xls.write_file(dat, output_path)
```
Observe that we need different paths if we want to read from CSV files and 
write to an Excel file.

📝 **Tip:** 
*Keep in mind that loading data from Excel files is typically much slower 
than loading data from CSV files. You will not see much difference if your 
tables have a few records. But if it has thousands of records, you 
definitely notice the difference.*

------------------------------------------------------------------------------
Next, we will talk about the implementation of the main engine.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../9_using_parameters/README.md
[next]: ../11_main_engine/README.md
[help]: ../../0_help/README.md
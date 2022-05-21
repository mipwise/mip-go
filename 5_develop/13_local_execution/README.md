# Local Execution
You have seen how to modify the `execute_locally.py` script to execute each 
type of the engines that we have created so far, namely, input actions, main 
engine, and output actions. However, making so many changes to the 
`execute_locally.py` script every time we want to execute a different engine 
is not convenient.

Typically, there is a convenient way to alternate between engines on an app. 
On Mip Hub, for instance, there is a drop-down menu from which users can 
select the engine they want to execute.

To have a similar experience when testing the package locally, we can use a 
more complete `execute_locally.py` script such as 
[the one](execute_locally.py) in this directory. Of course, you will have to 
adapt this script to your package.

## Executing from the command line
If you want to execute the main engine only, there is also the option of 
using the commandline.

All you have to do is to add a `__main__.py` file to the script's directory, 
i.e., the same directory that currently contains `main.py` and `schemas.py`,
and add the following content to it:

```python
from ticdat import standard_main
from mip_me import input_schema, output_schema, solve
if __name__ == "__main__":
    standard_main(input_schema, output_schema, solve)
```

Then you can execute the main engine from the commandline as follows:
```commandline
python -m mip_me -i test_mip_me/data/testing_data_1.xlsx -o 
test_mip_me/data/outputs
```

------------------------------------------------------------------------------

With this, we have implemented the first version of our solution and tested 
all the engines with a development instance. Later, we will implement unit 
testing as well. But before that, we will get our package ready for 
deployment on Mip Hub, so we can start to play with it on the internet browser.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../12_output_action/README.md
[next]: ../next_steps/README.md
[help]: ../../0_help/README.md
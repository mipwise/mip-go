# Python Package
As you may have realized, all the great stuff in Python is available in the 
form of packages, though you might not fully understand the reason behind 
that. *Pandas*, *NumPy*, *Matplotlib*, *scikit-learn*, are all examples of 
packages that you just import and start using in any project. That should 
not be a surprise.

What if you build some great stuff too (which you will soon)?  
How do you share it professionally with friends, collaborators, and clients?

The answer is **Python packages**.

And it might come as a big surprise for you that it's quite simple to create 
Python packages!

By the end of this section, you will have learned the importance of 
packaging solutions as well as how to create and use Python packages.

## Motivation
Imagine that you write a solution for a problem. You test it with your data 
and get so proud of your work that you decide to share your code with five 
friends of yours. Then you zip up the folder that contains the scripts and 
send it over to your friend. A few days later, you realize that there 
is a bug in your code, or you come up with a better version of the solution. 
Then you send new versions of the same script files. After a month, you have 
shared multiple versions and your friends start to reach out to you with 
suggestions or issues. That's when you find yourself spending a lot of time 
wading through multiple versions of your own code, trying to make sense of 
it while your friends are feeling frustrated and doubting whether they
should trust your solution. Finally, suppose that instead of friends, these 
people are actually your co-workers or clients! Not a good situation to be 
in, right?

The moral of the story, **proper code ought to be shared properly**. In the 
world of Python, it means creating packages that are systematically 
versioned, that can be installed and can be imported, just like Pandas, 
Matplotlib, and many others.

In fact, all you need to deploy an app on Mip Hub is to create a Python 
package that complies with some basic standards!

In other words, **we build packages to be installed or deployed**.

## Experiment 1
Let's run an experiment with the project we created in the
[New Project](../3_new_project/README.md) section. After adding
the `schemas.py` file to it, you should have something like this:

![Repository with Schemas](figures/repo_structure_with_schemas.png)

Now, open the Python Console in your project (not in the Mip Way project, it 
will only work in the project of your package) and type in `from XXX import 
schemas`, where `XXX` is the name of your script's directory (i.e., your
package). Then hit `ENTER`.

![Import Package in Console](figures/import_package_in_console.png)

Apparently, nothing has happened. But now, type in
`schemas.input_schema.schema()` and hit `ENTER`.  
What do you see? 

By doing this, you are calling the `schema` method of the `PanDatFactory` 
class. 

## Playing with OOP
Let's use this opportunity to learn some *object-oriented programming* (OOP),
just so that you can start to get familiar with it. 

So, try `schemas.input_schema.default_values`.  
What do you see this time? 

In this case, you are accessing
the `default_values` attribute of the `PanDatFactory` class.

You can try to call other methods and access other attributes. To see what 
is available, the first type in `schemas.input_schema` and when you type in the 
next dot, you will see a list of all methods and attributes (see the 
screenshot below). Some methods will require some type of argument that you 
might not have in this context, and hence you will not be able to call them. 
An example is the `create_full_parameters_dict` method, which requires a `dat` 
object that we will have later.

![Call Methods](figures/call_methods.png)

To summarize, once we get access to the `input_schema` object, which is an 
instance of the `PanDatFactory` class, we are able to access all of its 
methods and attributes.

## Experiment 2
Here is another experiment: instead of using the console, let's execute a 
code from a `.py` file.

So, first, let's create an `execute_locally.py` file inside the testing 
repository, `test_mip_me` in our case. 

📝 **Tip:** 
*It's a good practice to keep the package as clean as possible. Therefore, 
only files that are part of the solution should be kept inside the script's 
directory.*

The tip explains why we are creating the `execute_locally.py` file inside 
the testing repository, which is outside the package.

Now, enter the following lines of code in the `execute_locally.py` file:
```python
from mip_me import schemas
input_schema = schemas.input_schema
primary_keys = input_schema.primary_key_fields
print(primary_keys)
```

Execute the script (right-click in the editor and then **Run 
'execute_locally'**) to see the output in the **Run** tab. The output will 
be a dictionary showing the primary keys of each table in the input schema.

You could keep printing attributes to continue investigating the 
`input_schema` object. But there is a much more efficient way of doing this, 
which is using debugging.

## Debugging
Click next to the printing statement to set a breakpoint there.

![Run Debug](figures/run_debug.png)

Next, right-click in the editor and then **Debug 'execute_locally'**. Once 
the execution reaches your breakpoint, you can go to the **Variables** 
window and expand `primary_keys` to see its content. Alternatively, you can 
expand `input_schema`, and then `primary_key_fields`, which is the same thing.

![Explore Debug](figures/explore_debug.png)

## Adding the `__init__.py` file
Although we're able to import the `schemas` module by executing our scripts 
from the console and from a `.py` file, it should be noted that, if you try 
to execute these same scripts from other places, such as another project, 
it will not work because Python will not be able to find the modules of your 
project. It worked in the two experiments above because Pycharm executes 
the code from the root of the same project's repository.

So, if someone wanted to use our project, as it currently is, they would 
have to save a copy of the script's folder inside the repository of their 
project. 

Turns out that copying scripts around is a terrible way of distributing code!
We hope it's clear from the motivation section above.

The good news is that our simple project is on the right track and close to 
being considered a proper Python package!

As a next step, let's add an `__init__.py` file to the script's directory, 
i.e., the same directory that currently contains `main.py` and `schemas.py`,
and add the following content to it:

```python
__version__ = "0.1.0"
from mip_me.schemas import input_schema, output_schema
```

The first line is to provide the version of the package (we will discuss 
versioning later). In the second line, we import what we want the user of
our package to have access to in a convenient way.

What `__init__.py` does is to tell Python that that directory is a special 
one, a Python Package.

## Experiment 3
Let's go back to the `execute_locally.py` file and replace its content with 
the following:
```python
from mip_me import input_schema
primary_keys = input_schema.primary_key_fields
print(primary_keys)
```
Here is the previous version so you can compare:
```python
from mip_me import schemas
input_schema = schemas.input_schema
primary_keys = input_schema.primary_key_fields
print(primary_keys)
```
As you can see, we can now import `input_schema` directly from `mip_me` 
(which would not work without the import line we added to `__init__.py`). 
We can still import `schemas` like before, but we no longer need to.

## Experiment 4
As a final experiment, go to the Python console of your project (you might 
have to close the current console and open a new one), import your package, 
and look up its version.

![Package Version](figures/package_version.png)

You can do the same thing with any package that you have installed.

## Next steps
To summarize, we saw that:
* Using packages is the professional way to distribute Python code.
* To turn a directory into a package we only need to add an 
  `__init__.py` file to it.
* Objects imported in the `__init__.py` file become readily 
  available to users of the package.

In addition, you have learned how to:
* access methods and attributes of a Python object;
* create and execute a Python script;
* use the debugger and inspect objects;
* check the version of a package;

If you want to learn more about Python Packages, check out this 
[Python Packages][py_pkg] book, or at least spend 3 minutes reading the 
[introduction][py_pkg_intro] of the book.

------------------------------------------------------------------------------
The next step would be generating wheel files, or some other type of 
distribution files, so that anyone can install your package using `pip 
install`, for example. But first let's focus on developing the content of 
our Python package, testing it locally, and building better versions of it
in the Agile way.

[py_pkg]: https://py-pkgs.org/
[py_pkg_intro]: https://py-pkgs.org/01-introduction#introduction

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../4_data_schema/README.md
[next]: ../6_loading_data/README.md
[help]: ../../0_help/README.md
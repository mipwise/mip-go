# Default Deployment
Assuming that you developed your package using ticdat, like we 
did with our `mip_me` package, and generated the distribution
files, your package should be ready for a *default deployment*! 

A default deployment means that Mip Hub will apply
the default configuration to your app. But there is a lot
of flexibility to further customize your apps by simply populating
a few Python dictionaries. We will come back to that shortly.

## Uploading packages on Mip Hub
After login into https://apps.mipwise.com/, go to **Packages** and create a 
new package.

🗒️ **Note:** 
*Make sure that the name you enter exactly matches the name of the package 
(not considering versions) you will be uploading.*

Then, click on the *Manage Version* bottom (located under the **Actions** 
column on the right of the screen, next to the pen icon) to add a new
version of your package. When prompted, upload the distribution archive of 
your package, i.e., the `.tar.gz` file we generated in the 
[Distribution Package][distribution_package] section. The **Version** field 
will be populated automatically for you based on the package version you are 
uploading.

Once you are done, Mip Hub will validate your package. During that process, 
you will see **Running** in the status. Once done, the status will change to 
either **Successful** or **Failed**. 

If the package is validated successfully, then you are ready to deploy as 
many as you wish using this package!

If it fails, you can download the log to see what needs to be fixed.
Here are some common reasons that lead to validation failure:
* The package uses another package that is not listed in the
  `install_requires` of `setup.cfg`.
* One of the solve engines has an input argument that is not
  a `dat` or an `sln` object. Or it's an input action that
  doesn't return a `dat` object only. Or it's a main solve
  or an output action that doesn't return a `sln` object only.

## Deploying a new app
Once you have a package that has been successfully uploaded, you can click 
on the **New Application** button under the **Actions** column and fill in 
the missing information. Some fields will be automatically filled for you.
Once done, hit **Save** and go to **Applications**.

Alternatively, you can go to **Applications** first and create a new app 
by providing a name and selecting the uploaded version from there.

To see your app deployed, click on the **Manage Scenarios** bottom on the 
right of the **Application** window and next to the application you want to 
open. When you get inside the app for the first time, there will be one 
default scenario already created. You can edit any scenario after selecting 
it from the dropdown and clicking on the configuration button on the right. 
You can also create as many scenarios as you wish by clicking on the plus 
button on the right. These can be new empty scenarios or copies of existing 
ones. They will all look the same, except for their data.

## Uploading data
The first thing you may want to do when inside a new scenario is to upload 
data into it. It's possible to upload multiple tables in one go by clicking 
on the **Upload** button at the bottom of the screen, or you can upload only 
a specific table by selecting it and then clicking on **Table Options** and
**Import data**.

## Executing engines
Once you have uploaded all the required input data, you can go to the 
**Engines** tab to configure parameters and execute engines.

Even if your package doesn't have any actions, you will see two default 
actions called *Data Integrity Check*, one under *Input Actions* and another 
under *Output Actions*.

The first engine you may want to execute is the input data integrity check. 
Just select it from the dropdown and hit the green button. Then you can 
follow the progress in the log.

📝 **Tip:** 
*To hide the log, click on the maximize button located right below the 
execution button.*

Successful execution of a data integrity action means that the data is 
good, and you can move on to execute other engines. If the execution fails, 
you can see the data failure reports in the Inputs/Outputs Data Integrity
tables.

[distribution_package]: ../1_distribution_package/README.md

------------------------------------------------------------------------------
In the next section, you will learn how to customize several aspects of an app.

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../2_mip_hub/README.md
[next]: ../4_configured_deployment/README.md
[help]: ../../0_help/README.md
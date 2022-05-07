# Best Practices
Discovering and defining the problem are practices that we already consider 
part of our "best-practices catalog". But when it comes to development 
specifically, there are some key best practices that can improve the quality of
the overall solution tremendously.

Don't think of best practices as rules that must be followed, think of them 
as values to be cultivated.

Like safe driving, you would not take the highway with ten dogs messing 
around inside the car to put at risk the life of your family and the life 
of others just because there is no rule explicitly saying that you can't do 
that.

For example, at Mip Wise, we firmly believe that solutions should be 
reliable. So the reliability of a solution is a value that we cultivate. How?
By following best practices!

We will start discussing these best practices at a high level and then get 
more specific to provide extra guidance.

## Organized and Systematic (OSy)
Development is when you hand your well-defined problem over to the computer 
to be solved. Putting this way it may sound easier than it actually is. 
You know, computers are powerful, but you have to tell them
*exactly* what to do. But there is so much that you have to communicate
to your computer that, if you are not organized and systematic enough, you 
and your computer will not understand each other, which can turn out to be a 
catastrophe for the project.

So let's make it very clear: to develop a proper solution you must be as 
*organized and systematic* (OSy) as you can. Later, when someone asks you 
how did you build such a good solution, you can say that you were not lucky, 
you were OSy! 😄

By the way, this is not a rule, this is a principle. Machines are what they are.

You might be looking around right now and wondering: *How do these guys 
expect me to be OSy in developing a solution if I can't even manage to keep 
my desk organized?*

We know how! As Tony Robbins says, we are constantly making decisions to 
avoid pain and have pleasure in life. If the idea of cultivating values 
didn't buy you, and you are thinking that being OSy is going to be painful,
that's only because you have not felt the pain of debugging a messy code and 
the pleasure of seeing your tidy code returning reliable outputs. We will 
give our best to let you experience that pleasure as soon as possible, 
but we're also willing to let you feel the pain of dealing with a messy code 
if that's required for you to convince yourself how important it is to be OSy.

## Tidy, Tested, Safe (TTS)
Being organized and systematic is a high-level concept. To make it more 
practical and precise, let's have a look at the [Tidy, Tested, Safe][tts] 
(TTS) framework, which has been proposed by [Pete Cacioppi][pete], a very 
experienced programmer who is truly passionate about Python and solving 
real-world problems.

TTS provides a mental model to track key aspects of a maintainable and 
reliable solution. Next, we provide a quick overview of the framework. But we 
will dive deeper into these topics later on when it's appropriated.

[pete]: https://github.com/pjcpjc
[tts]: https://ttspython.org/

* **Tidy**
  Tidy is about organization and style. Not only does the code within a 
  script deserves to be organized, but also the directory that hosts the script 
  files and data, the git-flow strategy, documentation, etc. And there is no 
  need to reinvent the wheel here, it's just a matter of following 
  approaches that have already been proven efficient.

* **Tested**  
  To be reliable, the code must be tested. In Python especially, it's easy to 
  implement things in a hacky way that works for a given scenario. But 
  building an enterprise-grade application requires more than "Hey, it worked 
  now!". In fact, the best way to efficiently and reliably test your code is 
  by writing unit testing. And you will see that, in Python, doing automated 
  unit testing it's much easier than it might sound.

* **Safe**  
  Even a well-written and tested code can easily break if it can't handle bad 
  data. Naive developers will attempt to handle bad data by trying to guess 
  what can go wrong and implementing catches to handle the exceptions they have
  identified. However, it's nearly impossible to predict all that can go wrong 
  with data. So a much more systematic approach is required.

We summarize TTS with a quote from Pete:  
*Write normal Python. Automate the tests. Protect against dirty data.*

------------------------------------------------------------------------------
Next, you will start creating your first project, right here 
in Pycharm!

### [Home][home] | [Back][back] | [Next][next] | [Help][help]

[home]: ../../README.md
[back]: ../1_web_apps/README.md
[next]: ../3_new_project/README.md
[help]: ../../0_help/README.md

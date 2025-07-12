README

this here is my first README file. i plan on using it for notes on what this is, and why. so i, and YOU dont forget, or get confused

This is KDL, or kondikes debugging language. it will be used for replying scripts and functions in any python file, if set up correctly.
the vision:

* .bak files to be used, not the orignal(dont use .bak, use _KDL)
* watcher nodes for logging
* KCL commands. you know the commands future me, and if you forget we have a google doc for it, as well as the old KCL file

id say that sums it up nicly. uh, yeah. you can see the code comments, as well as __init__.py for whats needed

how to use. copy said file you are debugging into KDL folder. in Import_nexus from file import function(or *) and plug in calls to PLUGS, dicts are whatever arg needed for the function in CONTEXT. then run kernal. grasp function arg then said function should run.

Watcher or watcher nodes can be imported into the file you are debugging, call when needed, then boom. you have yourself a way to trace whats happening. you'll find what the watcher reports back with in the logs folder. 

KDLHandler is there for custom errors, feel free to implment your own and...

feel free to implment your own modules or features. its a debugging tool, form it, refine it, im not the best coder, so if there is somethings that could be better, refine it. MIT license for a reason.
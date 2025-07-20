from .Shell.cmd_kernal import cmd_prompt
from .Eyes.Watcher import __watcher__

# need this to run it as a package :)
__watcher__("kernal", "0", "KDL console booted", "cmd_kernal")
cmd_prompt() # run the cmd prompt
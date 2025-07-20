#stall, todo
import json
from colorama import Fore, Style, init
init(autoreset=True)

LOG_PATH1 = "./logs/TODO.log"
LOG_PATH2 = "./logs/TODO1.log"
LOG_PATH3 = "./logs/TODO2.log"

"""stall function/module for KDL debugging. you can compare this to the tooth pick on a swiss army knife, its not needed,
not even big, but its there, and has a use."""

def stall():
    print("this is a stall method. a place holder.")
    
#TODO __TODO__ function(ironic)

"""__TODO__ function will act like a watcher node, but more naggy(printing to the console, colored based text for priority)
and prioty based files(also in the log folder) no this will not be tagged to the file, since thats impossible"""

def __TODO__(todo, path, level):
    entry = {
        
        "action": todo,
        "where": path,
        "severity": level
    }
    
    if level == 0:
        LOG_PATH = LOG_PATH1
        color = Fore.LIGHTBLUE_EX
    elif level == 1:
        LOG_PATH = LOG_PATH2
        color = Fore.YELLOW
    elif level == 2:
        LOG_PATH = LOG_PATH3
        color = Fore.RED
    
    with open(LOG_PATH, "a") as log_file:
        log_file.write(json.dumps(entry, indent=2) + "\n")
    print(f"{Fore.LIGHTBLUE_EX}TODO: {todo}, {color}priority: {level}, {Fore.LIGHTBLUE_EX}where: {path}")
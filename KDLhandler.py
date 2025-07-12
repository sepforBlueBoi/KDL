#errors :D
from colorama import init, Fore, Back, Style
from Watcher import logging

init(autoreset=True) #colorma style rest after each print

watchtoggle = True # watcher node log toggle

class KDLErr:
    def grasperror(error_type, reason): # for grasp module
        print(Fore.RED + f"Grasp Error.{error_type}: " + Style.RESET_ALL + reason)
        if watchtoggle:
            logging("node 4: fork 1", "Error", "grasperror", f"a grasp error had been hit: {reason}")
        return
        
    def cmderror(error_type, reason): # for basic cmd errors
        print(Fore.RED +f"Cmd Error.{error_type}: " + Style.RESET_ALL + reason)
        if watchtoggle:
            logging("node 4: fork 2", "Error", "cmderror", f"a command error had been hit: {reason}")
        return
        
    def watchererror(error_type, reason): # for watcher nodes
        print(Fore.RED+ f"Watcher Node Error.{error_type}" + Style.RESET_ALL + reason)
        if watchtoggle:
            logging("node 4: fork 3", "Error", "watcherror", f"a watcher node has hit a error: {reason}")
        return
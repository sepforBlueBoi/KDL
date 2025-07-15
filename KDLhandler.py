#errors :D
from colorama import init, Fore, Style
from ErrEyes import Errorlog, init_erroreyes

init_erroreyes()


init(autoreset=True) #colorma style rest after each print

watchtoggle = True # watcher node log toggle

class KDLErr:
    def grasperror(error_type, reason): # for grasp module
        print(Fore.RED + f"Grasp Error.{error_type}: " + Style.RESET_ALL + reason)
        Errorlog("grasperror", reason)
        
    def cmderror(error_type, reason): # for basic cmd errors
        print(Fore.RED +f"Cmd Error.{error_type}: " + Style.RESET_ALL + str(reason))
        Errorlog("cmderror", reason)
        
    def watchererror(error_type, reason): # for Watcher node errors
        print(Fore.RED + f"Watcher Error. {error_type}: " + Style.RESET_ALL + str(reason))
        Errorlog("watchererror", reason)
        
        
    
        
#CMD_prompt
import time
from Parser.KDL_Parser import cmd_parser
from Eyes.Watcher import __watcher__, init_watcher
from Eyes.KDLhandler import KDLErr


err = KDLErr
init_watcher()
def cmd_prompt():
    print("=" * 40) # banner for info 
    print("Kondikes Debug Lens[KDL] v1.2.0") #1.2 now since grasp works for multiple context inputs
    print("Type 'help' for a list of commands.")
    print("Type 'exit' to quit.")
    print("For further info check 'README.md'.")
    print("=" * 40)
    
    while True: #loop
        try:
            cmd = input("\nKDL::> ").lower().strip() # cmd prompt duh
            for i in range(3):
                time.sleep(0.6) # a bit of stalling, makes it look like its doing something big
                print(".", end='', flush=True)
            print("\n")
                
            
            __watcher__("kernal", 1, f"cmd loading: {cmd}", "cmd_prompt")
            
            
            
            result = cmd_parser(cmd)
            
            if result == "exit":
                print("exiting...")
                __watcher__("kernal", 2, "exiting KDL", "cmd_prompt")
                time.sleep(1.2)
                break
            
        except KeyboardInterrupt:
            err.cmderror(KeyboardInterrupt, "ctrl c was pressed")
            break
        except Exception as e:
            
            err.cmderror("unknown", {e})
            continue
        

    
    
#CMD_prompt
import time
from KDL_Parser import cmd_parser
from Watcher import logging, init_watcher
from KDLhandler import KDLErr


err = KDLErr
init_watcher()
def cmd_prompt():
    print("=" * 40) # banner for info 
    print("Kondikes Debug Language[KDL] v1.1.0") #1.1 now since erreyes
    print("Type 'help' for a list of commands.")
    print("type 'exit' to quit.")
    print("=" * 40)
    
    while True: #loop
        try:
            cmd = input("\nKDL::> ").lower().strip() # cmd prompt duh
            for i in range(3):
                time.sleep(0.6) # a bit of stalling, makes it look like its doing something big
                print(".", end='', flush=True)
            print("\n")
                
            
            logging("node1", "Cmd input", cmd, "Command input in cmd_kernal. waiting for parsing")
            
            
            
            result = cmd_parser(cmd)
            
            if result == "exit":
                print("exiting...")
                time.sleep(1.2)
                break
            
        except KeyboardInterrupt:
            err.cmderror(KeyboardInterrupt, "ctrl c was pressed")
            break
        except Exception as e:
            logging("node2" ,"cmderror", "error in kernal", "a error occured")
            err.cmderror("unknown", {e})
            continue
        
if __name__ == "__main__":
    cmd_prompt() # run the cmd prompt
    
    
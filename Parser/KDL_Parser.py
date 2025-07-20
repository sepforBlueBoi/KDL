#parser
from .grasp_cmd import grasp
from ..Eyes.KDLhandler import KDLErr

err = KDLErr

def cmd_parser(cmd): # v1.0.0 for KDL parser. simple commands right now, but soon, it will grow.
    words = cmd.split()
    if not words:
       return "empty", []
    cmd = words[0] # splits the words up for the sake of things, come on, its a parser its what it does
    args = words[1:]
    if cmd == "help":
        print("Commands: ", #help command, 
            "\nExit: closes the interface",
            "\nHelp: shows this output. ",
            "\nGrasp: Used to Grasp functions.")
        
        if args:
           print(f"not sure why you said {args} afterwards though")
        return
           
    if cmd == "exit":
        return "exit"
           
    if cmd == "grasp": # checks for cmd, then calls upon grasp_cmd
        if not args:
            print("Grasp Failed. noting to grasp")
            
        plug_name = args[0]
        plug_args = args[1:] #parsing args for grasp
        return grasp(plug_name, plug_args)
    else:
        err.cmderror("keyword", "missing command keywords, or invalid command entered") #simple catch all,
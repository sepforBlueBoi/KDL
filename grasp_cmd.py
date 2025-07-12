#grasp
from Watcher import logging
from Cmd_Nexus import PLUGS, CONTEXT # imports plugs, explanentary
from KDLhandler import KDLErr

error = KDLErr
def grasp(plug_name, plug_args):
    logging("node3","grasp watcher 1", plug_name, plug_args)
    plug = PLUGS.get(plug_name) #sets up plug, so its easier for later.
    context = CONTEXT.get(plug_args[0]) if plug_args else None 
    
    if not plug:
        error.grasperror("plug_error", "plug name could not be found")
        return f":: Grasp Failed. Could not locate '{plug_name}'" # checkmate
    
    try:
        if context:
            return plug(context)
        else: # calls function based off of whats shown
            return plug()
    except Exception as e:
        error.grasperror(f"failed grasp", "refer to return method for reason")
        
        
    
        
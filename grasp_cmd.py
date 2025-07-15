#grasp
from Watcher import __watcher__
from Import_Nexus import PLUGS, CONTEXT # imports plugs, explanentary
from KDLhandler import KDLErr

error = KDLErr
def grasp(plug_name, plug_args):
    __watcher__("grasp", 1, f"function grasped: {plug_name, plug_args}", "grasp")
    plug = PLUGS.get(plug_name) #sets up plug, so its easier for later.
    #context = CONTEXT.get(plug_args[0:]) if plug_args else None 
    context = plug_args[0:] if len(plug_args) > 1 else [0]
    #context_more = plug_args[1:] if len(plug_args) > 1 else []
    
    if not plug:
        error.grasperror("plug_error", "plug name could not be found")
        return f":: Grasp Failed. Could not locate '{plug_name}'" # checkmate
    
    try:
        if context:
            #print(f"{plug.__name__} with {context if not context_more else context, context_more} has been called")
            return plug(*context)

        else: # calls function based off of whats shown
            return plug()
    except Exception as e:
        error.grasperror("failed grasp", f"{e}")
        
        
    
        
#imports here::
from Watcher import __watcher__ as watcher

# :: to here


PLUGS = { #plugs for functin calls, is very good for this. needs imports before anything can work, but trust
    "log": watcher
    
}
"""for above: {call_nick: call}"""
CONTEXT = {
    "node1": "kernal",
    "node2": "Parser",
    "node3": "grasp",
     #context, aka the arg or whatever said call needs.
     
}
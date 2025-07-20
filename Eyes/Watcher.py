# watcher node, aka my logger

import json
import time
import os
from .KDLhandler import KDLErr
err = KDLErr

WATCHER_NODE = {
    "kernal": "node 1",
    "parser": "node 2", #for organization
    "grasp": "node 3",
}
LOG_PATH = "./logs/watcher.log" #sets up pathway file

def init_watcher(): # adds pathway file, if it didnt exist before
    os.makedirs(LOG_PATH.rsplit("/", 1)[0], exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            f.write("")  # empty log file creation


def __watcher__(node, fork, event_type, source): # actual logging system, can and will be added upon later
    node_ = WATCHER_NODE.get(node)
    
    if not node:
        err.watchererror("NodeError", f"{node} not found")
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H: %M: %S"),
        "node type": {"type":node_, "fork": fork},
        "event": event_type,
        "source": source, # objects being logged
    }
    try:
        with open(LOG_PATH, "a") as log_file:
            log_file.write(json.dumps(entry, indent=2) + "\n") 
    except Exception as e:
        err.watchererror("NodeError", f"{node_}{fork} failed to report back: {e}")

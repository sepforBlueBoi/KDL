# watcher node, aka my logger

import json
import time
import os
from KDLhandler import KDLErr

err = KDLErr 

LOG_PATH = "./logs/watcher.log" #sets up pathway file

def init_watcher(): # adds [athway file, if it didnt exist before]
    os.makedirs(LOG_PATH.rsplit("/", 1)[0], exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            f.write("")  # empty log file creation


def logging(node, event_type, source, details): # actual logging system, can and will be added upon later
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H: %M: %S"),
        "node type": node,
        "event": event_type,
        "source": source, # objects being logged
        "details": details
    }
    try:
        with open(LOG_PATH, "a") as log_file:
            log_file.write(json.dumps(entry, indent=2) + "\n") 
    except Exception as e:
        err.watchererror("failed_log", {e})
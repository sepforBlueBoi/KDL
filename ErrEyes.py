import json
import time
import os

LOG_PATH = "./logs/watcher.erroreyes.log" #sets up pathway file


def init_erroreyes(): # adds [athway file, if it didnt exist before]
    os.makedirs(LOG_PATH.rsplit("/", 1)[0], exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w") as f:
            f.write("")  # empty log file creation

def Errorlog(event, details):
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H: %M: %S"),
        "event": event,
        # objects being logged
        "details": details
    }
    
    with open(LOG_PATH, "a") as log_file:
        log_file.write(json.dumps(entry, indent=2) + "\n") 
    

    
    
ONLY DEPENDENCY: COLORAMA

## 🧠 KDL: Kondike’s Debugging Language

**KDL** is a modular debugging framework for Python. Built to trace, log, and execute functions with contextual clarity.

Whether you’re wrangling simulations, testing plug chains, or architecting emergent systems, KDL gives you a real-time interface that's easy to use as soon as the watcher nodes, and functions are plugged in.

---

## 📐 Vision

KDL isn’t just a tool—it’s a lens, one could call it a langauge:

- 📁 `_KDL` files are not needed, but good for clarity
- 🕵️ Watcher nodes log system events with plug-level granularity
- 🧪 Plugs execute with context from `CONTEXT` and control from `PLUGS`
- 📜 KCL commands route actions, mutations, and simulations through grasp()

---

## ⚙️ Usage

### 1. Import Target
Copy your debug target into the KDL folder. In `Import_nexus.py`, register functions via:

```python
from target_file import target_function
```

### 2. Register Plug
In `PLUGS`, map your function:

```python
PLUGS = {
    "debug": target_function
}
```

### 3. Define Context
In `CONTEXT`, define necessary arguments:

```python
CONTEXT = {
    "debug_context": {"currency": 100, "traits": {"greed": True}}
}
"""or just the dict name if its already been laid out
and when importing mulitple args, only the first one needs to be mapped. other ones are not needed. cant be needed. """
```

### 4. Run Kernel
Use `grasp` to dispatch with context:

```bash
grasp debug debug_context
```

---
## How to use the Watcher nodes

### 1. Import watcher

```python
from Watcher import __watcher__
```

### 2. Call

To Use the watcher node call the function, with arguments.
Example:
```python
__watcher__("grasp", 599, "function grasped", "grasp")
```

The arguments should line up like so:

- 1. node type. check in Watcher.py for node types, can be expanded on

- 2. Node ID aka the fork. either run the fork ID call based, or top to bottem based
    - Call based is each call gets its own set of forks, still top to bottem, or bottem to top, but each function should get its own fork 1.

    - top to bottem based. python runs code top to bottem, so thats how these are laid out, the call at to very tippy top of the code will be 1, or 0, bottem will be...well depends on how many calls you have. or reverse it bottem to top.

- 3. Event type, self explanatory, the event you're logging

- 4. Source, Class, function, or file its in. allows for different forks for different functions or even classes.

---
## Example Output
After each command input, it should load a bit. if you want this can be removed. other wise it should have three dots that signify the loading. grasp has the print that says it works: 

```python
print(f"{plug.__name__} with {context if not context_more else context, context_more} has been called")
```

also runs the function, thats the other show.

`__watcher__` does not print to the console, but you can find it in the logs folder. also error eyes does the same to its own file, same folder
---

## 🔍 Debugging Tools

- **Watcher Nodes** — passive loggers writing structured traces to `logs/`
- **KDLErr (KDLhandler)** — modular error handler with color-coded output and toggleable logging
- **ErrEyes(Error Eyes)** — watcher nodes for KDLErr errors
- **grasp()** — dynamic command dispatcher with context injection and lifecycle tracing

---

## 🧪 Philosophy

KDL is meant to be changed. Fork it, refine it, build your own plugs, handlers, and nodes. It’s under the MIT License so you have full freedom to shape it into what *you* need.

---

most of this README is ai generated, to tired from working on the code, but it has been edited. 

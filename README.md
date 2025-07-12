ONLY DEPENDENCY: COLORAMA

## 🧠 KDL: Kondike’s Debugging Language

**KDL** is a modular debugging framework for Python. Built to trace, log, and execute functions with contextual clarity and storytelling flair.

Whether you’re wrangling simulations, testing plug chains, or architecting emergent systems, KDL gives you a real-time interface where code speaks and structure listens.

---

## 📐 Vision

KDL isn’t just a tool—it’s a philosophy:

- 📁 `_KDL` files define intent and architecture (not disposable backups)
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
or just the dict name if its already been laid out
```

### 4. Run Kernel
Use `grasp` to dispatch with context:

```bash
grasp debug debug_context
```

---

## 🔍 Debugging Tools

- **Watcher Nodes** — passive loggers writing structured traces to `logs/`
- **KDLErr (KDLhandler)** — modular error handler with color-coded output and toggleable logging
- **grasp()** — dynamic command dispatcher with context injection and lifecycle tracing

---

## 🧪 Philosophy

KDL is meant to be changed. Fork it, refine it, build your own plugs, handlers, and nodes. It’s under the MIT License so you have full freedom to shape it into what *you* need.

---

this was ai generated, i dont feel like making a readme file ;)


I desire to invoke one sub-application from another sub-application.
To do so is cumbersome, because I must construct a command-line and then
invoke the subcommand via `subprocess` like so:

```python
cmdline = f'python main-app.py greet --greeting {file_name} --name {file_size}'.split()
subprocess.run(cmdline)
```

Instead of constructing a command-line, I wish to make a method call from the
`start()` method of one sub-application to invoke the other sub-application
like so:

```python
    arg = dict(greeting=file_name, name=file_size)
    greet_app = Greeting(**arg)
    greet_app.launch_instance()
```

but calling `launch_instance()` leads to the following error:

```
traitlets.config.configurable.MultipleInstanceError: 
   An incompatible sibling of 'Greeting' is already 
   instanciated as singleton: File
```

So, to remedy this problem, if one could replace the current 
singleton-sub-application with another programmatically, then one would
not have to resort to making shell calls to do so.

So, the request is a method like `replace_instance()` or `exec_instance` 
that gets around the singleton issue.

# Source code to replicate the error

https://github.com/metaperl/traitlets-lab/tree/main/tds-variation


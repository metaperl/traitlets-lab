This is a variation on [the Towards Data Science article](https://towardsdatascience.com/tutorial-create-a-python-cli-package-a2410b47af35).

I want to experiment with 
* invoking a sub-command from another sub-command without 
resorting to making shell calls.

# To this end, we start with 2 sub-applications:

## Greeting sub-application

This subapp prints `"f{greeting} {name}{punctuation}"` where all 3 are configurable
from the command-line. Examples:

    shell> python cli_apps.py greet --Greeting.greeting yo
yo, World!

    shell> python cli_apps.py greet --Greeting.name dude
Hello, dude!

    shell> python cli_apps.py greet --Greeting.punctuation ?
Hello, World?

## File sub-application

This subapp prints the full path to a file and optionally shows the size of it:

    shell> python cli_apps.py file --File.file README.md
    C:\programming\traitlets-lab\tds-variation\README.md

    shell> python cli_apps.py file --File.file README.md --File.show_size True
    C:\programming\traitlets-lab\tds-variation\README.md
        size: 811 bytes

# And now to get to the experiment:

How can I call the greeting subapp from the file subapp like so:

    shell> python cli_apps.py file --File.file README.md --File.as_greeting True


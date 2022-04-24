from traitlets.config import Application

from subapps.greet_app import Greeting
from subapps.file_app import File


class CLIapp(Application):
    subcommands = dict(
        greet=(
            Greeting,
            """
            Prints a greeting!
            """.strip()
        ),

        file=(
            File,
            """
            Prints the absolute path for a file!
            """.strip()
        ),
    )

    def start(self):
        if self.subapp is None:
            print("""No command given (run with --help for options).
                  List of subcommands:\n""")
            self.print_subcommands()
        super(CLIapp, self).start()


def main():
    CLIapp.launch_instance()


if __name__ == '__main__':
    main()

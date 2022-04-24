import os

from traitlets import Bool, Unicode, Integer
from traitlets.config import Application


class File(Application):
    size = Integer()
    show_size = Bool(False, "Show size of file also?").tag(config=True)
    file = Unicode(help="Relative path to file to process.").tag(config=True)
    as_greeting = Bool(False, help="Call greet app to render file data as a greeting.").tag(config=True)

    def start(self):

        self.file = os.path.abspath(self.file)
        self.size = os.path.getsize(self.file)

        if self.as_greeting:
            from subapps.greet_app import Greeting
            arg = dict(greeting=self.file, punctuation='bytes')
            if self.show_size:
                arg['name'] = self.size
            greet_app = Greeting(**arg)
            greet_app.launch_instance()
        else:
            print(self.file)
            if self.show_size:
                print(f'\tsize: {self.size} bytes')


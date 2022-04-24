from traitlets.config import Application
from traitlets import Unicode


class Greeting(Application):
    greeting = Unicode("Hello").tag(config=True)
    name = Unicode("World").tag(config=True)
    punctuation = Unicode("!").tag(config=True)

    def start(self):
        print(self.greeting + ", " + self.name + self.punctuation)

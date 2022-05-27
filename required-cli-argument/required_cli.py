from traitlets.config import Application
from traitlets import List, Dict, Integer, Unicode, validate, TraitError


class App(Application):

    aliases = {"x": "App.x", "y": "App.y"}
    x = Unicode().tag(config=True)
    y = Unicode().tag(config=True)


    @validate('x')
    def _valid_x(self, proposal):
        print(f"Attempting to validate {proposal['value']}")
        if proposal['value'] % 2 != self.parity:
            raise TraitError('data and parity should be consistent')
        return proposal['value']

    def start(self):
        print(f"typex = {type(self.x)} val={self.x}")
        print(f"y={self.y}")

        self.x = "hi"


if __name__ == "__main__":
    App.launch_instance()

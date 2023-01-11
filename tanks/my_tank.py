"""Bare-bones Python code-tanks tank
"""

from codetanks import BaseTank, commands


class MyTank(BaseTank):
    """Bare-bones Python code-tanks tank
    """

    def __init__(self):
        super().__init__()

        print('Running my tank!')

    def run(self):
        # TODO: implement
        pass

    def on_event(self, event):
        # TODO: implement
        pass


def create_tank():
    """Return an instance of your tank
    """
    return MyTank()

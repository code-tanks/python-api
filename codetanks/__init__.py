"""The BaseTank class defines the structure of a tank object
"""

from abc import ABC, abstractmethod


class BaseTank(ABC):
    """
    The BaseTank class defines the structure of a tank object

    ...
    Attributes
    ----------
    commands: list[int]
        buffer of commands

    Methods
    -------
    run()
        called by the server to collect buffer of commands

    on_event(event)
        called by the server upon a event to collect buffer of commands
    """

    def __init__(self):
        print('Started Tank')
        self.commands: list[int] = []

    @abstractmethod
    def run(self):
        """called by the server to collect buffer of commands
        """

    @abstractmethod
    def on_event(self, event):
        """called by the server upon a event to collect buffer of commands
        """

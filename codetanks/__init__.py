import codetanks.commands
from abc import ABC, abstractmethod


class BaseTank(ABC):
    def __init__(self):
        print('Started Tank')
        self.commands = []

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def on_event(self, event_type, info):
        pass

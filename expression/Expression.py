
from abc import ABC, abstractmethod


class Expression(ABC):

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def evaluate(self, context):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def toMiniString(self):
        pass
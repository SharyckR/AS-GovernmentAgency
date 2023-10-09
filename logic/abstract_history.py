from abc import ABC, abstractmethod

from pydantic import BaseModel


class AbstractHistory(ABC, BaseModel):
    """
    Abstract base class for history objects.

    Attributes:
        None

    Methods:
        __str__(): Returns a string representation of the history.
        __eq__(other): Compares two history objects to check if they are equal.
    """
    @abstractmethod
    def __str__(self):
        """
        Returns a string representation of the history.

        Returns:
            str: A string containing history information.
        """
        pass

    @abstractmethod
    def __eq__(self, other):
        """
        Compares two history objects to check if they are equal.

        Args:
            other: Another history object to compare.

        Returns:
            bool: True if the histories are equal, False otherwise.
        """
        pass

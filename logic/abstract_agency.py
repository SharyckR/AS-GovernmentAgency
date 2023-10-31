from abc import ABC, abstractmethod
from pydantic import BaseModel


class AbstractAgency(ABC, BaseModel):
    """
    Abstract base class for agency objects.
    Methods:
        __str__(): Returns a string representation of the agency.
        __eq__(other): Compares two agency objects to check if they are equal.
    """
    @abstractmethod
    def __str__(self):
        """
        Returns a string representation of the agency.
        """
        pass

    @abstractmethod
    def __eq__(self, other):
        """
        Compares two agency objects to check if they are equal.
        Args:
            other: Another agency object to compare.

        Returns:
            bool: True if the agencies are equal, False otherwise.
        """
        pass

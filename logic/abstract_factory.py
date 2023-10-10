from abc import ABC, abstractmethod
from pydantic import BaseModel
from logic.abstract_agency import AbstractAgency
from logic.abstract_history import AbstractHistory


class AbstractFactory(ABC, BaseModel):
    """
    Abstract Factory class for creating agency and history objects.

    Attributes:
        None

    Methods:
        create_agency(): Create an instance of an AbstractAgency.
        create_history(): Create an instance of an AbstractHistory.
    """
    @abstractmethod
    def create_agency(self) -> AbstractAgency:
        """
        Create an instance of an AbstractAgency.

        Returns:
            AbstractAgency: An instance of AbstractAgency or its subclass.
        """
        pass

    @abstractmethod
    def create_history(self) -> AbstractHistory:
        """
        Create an instance of an AbstractHistory.

        Returns:
            AbstractHistory: An instance of AbstractHistory or its subclass.
        """
        pass

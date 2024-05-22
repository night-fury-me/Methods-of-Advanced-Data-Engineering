# project-root/etl-components/validate/validator.py

from abc import ABC, abstractmethod

class Validator(ABC):
    """
    Interface for data validation.
    """

    @abstractmethod
    def validate_data(self):
        pass

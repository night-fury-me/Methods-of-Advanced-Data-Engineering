# project-root/etl-components/store/storer.py

from abc import ABC, abstractmethod

class Storer(ABC):
    """
    Inteface for storing raw data locally
    """

    @abstractmethod
    def store_data(self):
        pass
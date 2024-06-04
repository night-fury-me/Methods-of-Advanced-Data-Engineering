# project-root/etl-components/load/loader.py

from abc import ABC, abstractmethod

class Loader(ABC):
    """
    Inteface for data loading
    """

    @abstractmethod
    def load_data(self, read_from, write_to, database_name):
        pass
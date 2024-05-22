# project-root/etl-components/extract/extractor.py

from abc import ABC, abstractmethod

class Extractor(ABC):
    """
    Inteface for data extraction
    """

    @abstractmethod
    def extract_data(self):
        pass
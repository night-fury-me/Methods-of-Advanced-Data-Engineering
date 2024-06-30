# project-root/etl-components/transform/transformer.py

from abc import ABC, abstractmethod

class Transformer(ABC):
    """
    Interface for data transformation.
    """

    @abstractmethod
    def transform_data(self, read_from, write_to, dataset_name):
        pass

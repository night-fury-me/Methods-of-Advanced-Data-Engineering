import os
import pandas as pd # type: ignore

from .extractor import Extractor
from logger import BaseLogger

class CsvExtractor(Extractor):

    def __init__(self, logger: BaseLogger, delimeter = None) -> None:
        self.delimeter = delimeter
        self.logger = logger

    def extract_data(self, extract_from, extract_to, dataset_name):
        
        try:
            if not os.path.exists(extract_to):
                os.makedirs(extract_to)

            data = pd.read_csv(extract_from, delimiter=self.delimeter)
            data.to_csv(f"{extract_to}/{dataset_name}.csv")

            self.logger.info(f"Data extracted and saved to: {extract_to}")
        except Exception as ex:
            self.logger.error(f"Error while extracting data: {ex}")
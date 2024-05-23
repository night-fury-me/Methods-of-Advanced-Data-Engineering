import os
import pandas as pd # type: ignore
from utils import logger

from .extractor import Extractor

class CsvExtractor(Extractor):

    def __init__(self, delimeter = None) -> None:
        self.delimeter = delimeter

    def extract_data(self, extract_from, extract_to, dataset_name):
        
        try:
            if not os.path.exists(extract_to):
                os.makedirs(extract_to)

            data = pd.read_csv(extract_from, delimiter=self.delimeter)
            data.to_csv(f"{extract_to}/{dataset_name}.csv")

            logger.info(f"Data extracted and saved to: {extract_to}")
        except Exception as ex:
            logger.error(f"Error while extracting data: {ex}")
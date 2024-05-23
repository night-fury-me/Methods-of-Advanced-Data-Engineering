
import os
import csv
import requests
from utils import logger

from .extractor import Extractor

class CsvExtractor(Extractor):

    def extract_data(self, extract_from, extract_to, dataset_name):
        
        try:
            if not os.path.exists(extract_to):
                os.makedirs(extract_to)

            with requests.get(extract_from) as response:
                response.raise_for_status()
                data = response.text
                csv_file_path = f"{extract_to}/{dataset_name}.csv"

                with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
                    writer = csv.writer(csv_file)
                    for line in data.splitlines():
                        writer.writerow(line.split(','))

            logger.info(f"Data extracted and saved to: {extract_to}")
        except Exception as ex:
            logger.error(f"Error while extracting data: {ex}")
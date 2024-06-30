import os
import pandas as pd # type: ignore
from .transformer import Transformer
from logger import BaseLogger

class SolarFlareDataTransformer(Transformer):

    def __init__(self, logger: BaseLogger) -> None:
        super().__init__()
        self.logger = logger

    def transform_data(self, read_from, write_to, dataset_name):

        try:
            data = pd.read_csv(read_from)
            data.rename(columns={'T_REC': 'Date'}, inplace=True)
            data['Date'] = pd.to_datetime(data['Date'])
            data.dropna()

            if not os.path.exists(write_to):
                os.makedirs(write_to)
            
            output_path = os.path.join(write_to, f"{dataset_name}.csv")
            data.to_csv(output_path, index=False, header=True)

            self.logger.info(f"Data transformation successful.")

        except Exception as ex:
            self.logger.error(f"Error occured while transforming data: {ex}")

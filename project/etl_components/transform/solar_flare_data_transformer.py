import os
import pandas as pd # type: ignore
from utils import logger
from .transformer import Transformer


class SolarFlareDataTransformer(Transformer):

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

            logger.info(f"Data transformation successful.")

        except Exception as ex:
            logger.error(f"Error occured while transforming data: {ex}")

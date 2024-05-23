import os
import pandas as pd # type: ignore
from utils import logger
from .transformer import Transformer


class SeaLevelDataTransformer(Transformer):

    def transform_data(self, read_from, write_to, dataset_name):

        try:
            data = pd.read_csv(read_from)
            data_subset = data[['Measure', 'Date', 'Value']]

            data_subset.columns = ['Sea_Name', 'Date', 'Sea_Level_MM']

            data_subset.loc[:, 'Date'] = pd.to_datetime(data_subset['Date'], format='D%m/%d/%Y').dt.strftime('%Y-%m-%d %H:%M:%S')
            data_subset.dropna()
            
            if not os.path.exists(write_to):
                os.makedirs(write_to)
            
            output_path = os.path.join(write_to, dataset_name)
            data_subset.to_csv(output_path, index=False, header=True)

            logger.info(f"Data transformation successful.")

        except Exception as ex:
            logger.error(f"Error occured while transforming data: {ex}")

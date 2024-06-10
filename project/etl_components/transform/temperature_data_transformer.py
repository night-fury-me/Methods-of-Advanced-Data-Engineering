import os
import pandas as pd # type: ignore
from .transformer import Transformer
from logger import BaseLogger

class TemperatureDataTransformer(Transformer):

    def __init__(self, logger: BaseLogger) -> None:
        super().__init__()
        self.logger = logger

    def transform_data(self, read_from, write_to, dataset_name):

        try:
            data = pd.read_csv(read_from)
            choosen_columns  = ['Country', 'ISO3'] 
            choosen_columns += [col for col in data.columns if col.startswith('F')]
            
            data_filtered    = data[choosen_columns]
            data_filtered    = data_filtered.loc[:, ~data_filtered.columns.str.contains('Unnamed', case = False)] 

            data_melted = pd.melt(
                data_filtered, 
                id_vars     = ['Country', 'ISO3'], 
                var_name    = 'Date', 
                value_name  = 'Temp_Change'
            )

            data_melted['Date'] = data_melted['Date'].str.extract(r'F(\d+)').astype(int)
            data_melted['Date'] = pd.to_datetime(data_melted['Date'], format='%Y').dt.strftime('%Y-%m-%d %H:%M:%S')
            data_melted = data_melted.dropna()

            if not os.path.exists(write_to):
                os.makedirs(write_to)
            
            output_path = os.path.join(write_to, f"{dataset_name}.csv")
            data_melted.to_csv(output_path, index = False, header = True)
            
            self.logger.info(f"Data transformation successful.")

        except Exception as ex:
            self.logger.error(f"Error occured while transforming data: {ex}")

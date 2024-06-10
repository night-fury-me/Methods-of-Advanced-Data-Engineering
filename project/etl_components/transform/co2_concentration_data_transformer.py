import os
import pandas as pd # type: ignore
from .transformer import Transformer
from logger import BaseLogger

class Co2ConcentrationDataTransformer(Transformer):

    def __init__(self, logger: BaseLogger) -> None:
        super().__init__()
        self.logger = logger

    def transform_data(self, read_from, write_to, dataset_name):

        try:
            data = pd.read_csv(read_from)

            data_subset = data.loc[:, ~data.columns.str.contains('Unnamed', case = False)]
            data_subset = data_subset[['Date', 'Value']]
            data_subset.columns = ['Date', 'CO2_Concentration_PPM']
            data_subset.loc[:, 'Date'] = pd.to_datetime(data_subset['Date'], format='%YM%m').dt.strftime('%Y-%m-%d %H:%M:%S')
            data_subset = data_subset.dropna()

            if not os.path.exists(write_to):
                os.makedirs(write_to)
            
            output_path = os.path.join(write_to, f"{dataset_name}.csv")
            data_subset.to_csv(output_path, index=False, header=True)

            self.logger.info(f"Data transformation successful")

        except Exception as ex:
            self.logger.error(f"Error occured while transforming data: {ex}")

import unittest
import pandas as pd

from etl_components import Co2ConcentrationDataTransformer, Transformer
from logger import BaseLogger, ConsoleLogger
from .mock_data import CO2_Concentration_Mock_Data

class TestTransform(unittest.TestCase):

    def test_transform_data(self):
        
        read_from = "./tests/mock_data/CO2_Concentration_Mock_Data.csv"
        write_to = "./tests/mock_data/"
        dataset_name = "Transformed_CO2_Concentration_Mock_Data"
        
        # Save mock data locally
        CO2_Concentration_Mock_Data.to_csv(read_from)

        console_logger: BaseLogger = ConsoleLogger()

        transformer: Transformer = Co2ConcentrationDataTransformer(logger = console_logger)
        transformer.transform_data(read_from, write_to, dataset_name)

        expected_columns = ['Date', 'CO2_Concentration_PPM']

        transformed_data = pd.read_csv('./tests/mock_data/Transformed_CO2_Concentration_Mock_Data.csv')

        self.assertEqual(
            expected_columns, 
            transformed_data.columns.to_list(), 
            msg = "Resulting dataset should contain 'Date' and 'CO2_Concentration_PPM' column."
        )
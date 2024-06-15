import unittest
import pandas as pd
import os

from etl_components import (
    Transformer,
    Co2ConcentrationDataTransformer,
    SolarFlareDataTransformer,
    TemperatureDataTransformer
)

from .mock import (
    MockLogger,
    CO2_Concentration_Mock_Data,
    Solar_Flare_Mock_Data,
    Temperature_Change_Mock_Data
)

RAW_DATA_DIR = "./tests/mock/data/raw/"
TRANSFORMED_DATA_DIR = "./tests/mock/data/transformed/"

class TestTransform(unittest.TestCase):

    def test_co2_concentration_data_transformation(self):
        
        dataset_name = "CO2_Concentration_Mock_Data"
        raw_data_path = os.path.join(RAW_DATA_DIR, f"{dataset_name}.csv")
        transformed_data_path = os.path.join(TRANSFORMED_DATA_DIR, f"{dataset_name}.csv")

        # Save mock data locally
        CO2_Concentration_Mock_Data.to_csv(raw_data_path)

        mock_logger = MockLogger()

        transformer: Transformer = Co2ConcentrationDataTransformer(logger = mock_logger)
        transformer.transform_data(
            read_from       = raw_data_path, 
            write_to        = TRANSFORMED_DATA_DIR, 
            dataset_name    = dataset_name
        )

        expected_columns = ['Date', 'CO2_Concentration_PPM']
        expected_columns = set(expected_columns)

        transformed_data = pd.read_csv(transformed_data_path)
        resulting_columns = set(transformed_data.columns.to_list())

        column_difference = expected_columns - resulting_columns

        self.assertEqual(
            len(column_difference), 0, 
            msg = "Resulting dataset should contain same number of columns with same name."
        )

    def test_solar_flare_data_transformation(self):

        dataset_name = "Solar_Flare_Mock_Data"
        raw_data_path = os.path.join(RAW_DATA_DIR, f"{dataset_name}.csv")
        transformed_data_path = os.path.join(TRANSFORMED_DATA_DIR, f"{dataset_name}.csv")

        # Save mock data locally
        Solar_Flare_Mock_Data.to_csv(raw_data_path)

        mock_logger = MockLogger()

        transformer: Transformer = SolarFlareDataTransformer(logger = mock_logger)
        transformer.transform_data(
            read_from       = raw_data_path, 
            write_to        = TRANSFORMED_DATA_DIR, 
            dataset_name    = dataset_name
        )

        expected_columns = ['FlareNumber', 'Date', 'NOAA_AR', 'QUALITY', 'Longitude', 'Latitude', 'TOTUSJH', 'TOTBSQ', 'TOTPOT', 'TOTUSJZ', 'ABSNJZH', 'SAVNCPP', 'USFLUX', 'AREA_ACR', 'TOTFZ', 'MEANPOT', 'R_VALUE', 'EPSZ', 'SHRGT45', 'MEANSHR', 'MEANGAM', 'MEANGBT', 'MEANGBZ', 'MEANGBH', 'MEANJZH', 'TOTFY', 'MEANJZD', 'MEANALP', 'TOTFX', 'EPSY', 'EPSX']
        expected_columns = set(expected_columns)

        transformed_data = pd.read_csv(transformed_data_path)
        resulting_columns = set(transformed_data.columns.to_list())

        column_difference = expected_columns - resulting_columns

        self.assertEqual(
            len(column_difference), 0, 
            msg = "Resulting dataset should contain same number of columns with same name."
        )

    def test_temperature_change_data_transformation(self):

        dataset_name = "Temperature_Change_Mock_Data"
        raw_data_path = os.path.join(RAW_DATA_DIR, f"{dataset_name}.csv")
        transformed_data_path = os.path.join(TRANSFORMED_DATA_DIR, f"{dataset_name}.csv")

        # Save mock data locally
        Temperature_Change_Mock_Data.to_csv(raw_data_path)

        mock_logger = MockLogger()

        transformer: Transformer = TemperatureDataTransformer(logger = mock_logger)
        transformer.transform_data(
            read_from       = raw_data_path, 
            write_to        = TRANSFORMED_DATA_DIR, 
            dataset_name    = dataset_name
        )

        expected_columns = ['Country', 'ISO3', 'Date', 'Temp_Change']
        expected_columns = set(expected_columns)

        transformed_data = pd.read_csv(transformed_data_path)
        resulting_columns = set(transformed_data.columns.to_list())

        column_difference = expected_columns - resulting_columns

        self.assertEqual(
            len(column_difference), 0, 
            msg = "Resulting dataset should contain same number of columns with same name."
        )
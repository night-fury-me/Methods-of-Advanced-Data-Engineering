import unittest
import os
import sqlite3
import pandas as pd

from etl_components import (
    Extractor,
    CsvExtractor,
    Transformer,
    Co2ConcentrationDataTransformer,
    Loader,
    SQLiteLoader
)
from logger import BaseLogger, ConsoleLogger
from tasks import Task, TaskPipeline, PipelineQueue

from .mock_data import CO2_Concentration_Mock_Data

class TestPipeline(unittest.TestCase):
    def test_co2_concentration_pipeline(self):
        
        # Setup test environment
        read_from = "./tests/mock_data/CO2_Concentration_Mock_Data.csv"
        write_to = "./tests/mock_data/"
        raw_dataset_name = "Transformed_CO2_Concentration_Mock_Data"
        transformed_dataset_name = "Transformed_CO2_Concentration_Mock_Data"
        transformed_dataset_path = "./tests/mock_data/Transformed_CO2_Concentration_Mock_Data.csv"
        db_name = 'dataset.sqlite'
        pipeline_name = 'Test Pipeline'

        # Save mock data locally
        logger: BaseLogger = ConsoleLogger()
        CO2_Concentration_Mock_Data.to_csv(read_from)

        # Extract
        extractor: Extractor = CsvExtractor(logger)
        extract = Task(
            name    = 'Data Extractor',
            action  = lambda: extractor.extract_data(
                extract_from = read_from,
                extract_to   = write_to,
                dataset_name = raw_dataset_name
            ),
            logger = logger
        )

        # Transform
        transformer: Transformer = Co2ConcentrationDataTransformer(logger)
        transform = Task(
            name    = 'Data Transformation',
            action  = lambda: transformer.transform_data(
                read_from       = read_from,
                write_to        = write_to,
                dataset_name    = transformed_dataset_name
            ),
            logger  = logger
        )

        # Load
        loader: Loader = SQLiteLoader(logger)
        load = Task(
            name    = 'Data Loader',
            action  = lambda: loader.load_data(
                read_from       = write_to,
                write_to        = write_to,
                database_name   = db_name
            ),
            logger  = logger
        )

        test_pipeline = TaskPipeline(pipeline_name, logger)
        
        (
            test_pipeline
                >> extract 
                    >> transform
                        >> load
        )
        
        test_pipeline_queue = PipelineQueue()
        test_pipeline_queue.push(test_pipeline)
        test_pipeline_queue.run()

        conn = sqlite3.connect(os.path.join(write_to, db_name))
        saved_final_test_data = None
        saved_final_test_data = pd.read_sql(
            sql = f"SELECT * FROM 'Transformed_CO2_Concentration_Mock_Data'",
            con = conn
        )
        conn.close()
        
        self.assertEqual(len(saved_final_test_data), 10)
        self.assertEqual(len(saved_final_test_data.columns.to_list()), 2)
        self.assertEqual(saved_final_test_data.columns.to_list(), ['Date', 'CO2_Concentration_PPM'])
        



        


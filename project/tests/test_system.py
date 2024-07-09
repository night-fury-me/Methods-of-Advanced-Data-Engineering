import unittest
import os
import sqlite3
import pandas as pd

from ETL import (
    Extractor,
    CsvExtractor,
    Transformer,
    Co2ConcentrationDataTransformer,
    Loader,
    SQLiteLoader
)

from tasks import Task, TaskPipeline, PipelineQueue

from .mock import (
    MockLogger,
    CO2_Concentration_Mock_Data
)

RAW_DATA_DIR = "./tests/mock/data/raw/"
TRANSFORMED_DATA_DIR = "./tests/mock/data/transformed/"
SINK_DATA_DIR = "./tests/mock/data/sink/"

class TestPipeline(unittest.TestCase):
    def test_co2_concentration_pipeline(self):
        
        # Setup test environment
        dataset_name = "Data_For_Pipeline_Test"
        raw_data_path = os.path.join(RAW_DATA_DIR, f"{dataset_name}.csv")
        transformed_data_path = os.path.join(TRANSFORMED_DATA_DIR, f"{dataset_name}.csv")

        db_name = 'dataset.sqlite'
        pipeline_name = 'Test Pipeline'

        sqlite_db_path = os.path.dirname(os.path.join(SINK_DATA_DIR, db_name))
        os.makedirs(sqlite_db_path, exist_ok = True)    

        # Save mock data locally
        logger = MockLogger()
        CO2_Concentration_Mock_Data.to_csv(raw_data_path)

        # Extract
        extractor: Extractor = CsvExtractor(logger)
        extract = Task(
            name    = 'Data Extractor',
            action  = lambda: extractor.extract_data(
                extract_from = raw_data_path,
                extract_to   = RAW_DATA_DIR,
                dataset_name = dataset_name
            ),
            logger = logger
        )

        # Transform
        transformer: Transformer = Co2ConcentrationDataTransformer(logger)
        transform = Task(
            name    = 'Data Transformation',
            action  = lambda: transformer.transform_data(
                read_from       = raw_data_path,
                write_to        = TRANSFORMED_DATA_DIR,
                dataset_name    = dataset_name
            ),
            logger  = logger
        )

        # Load
        loader: Loader = SQLiteLoader(logger)
        load = Task(
            name    = 'Data Loader',
            action  = lambda: loader.load_data(
                read_from       = TRANSFORMED_DATA_DIR,
                write_to        = SINK_DATA_DIR,
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

        conn = sqlite3.connect(os.path.join(SINK_DATA_DIR, db_name))
        saved_final_test_data = None
        saved_final_test_data = pd.read_sql(
            sql = f"SELECT * FROM '{dataset_name}'",
            con = conn
        )
        conn.close()
        
        # For testing purpose.
        self.assertEqual(True, False)

        self.assertEqual(len(saved_final_test_data), 10)
        self.assertEqual(len(saved_final_test_data.columns.to_list()), 2)
        self.assertEqual(saved_final_test_data.columns.to_list(), ['Date', 'CO2_Concentration_PPM'])
        



        


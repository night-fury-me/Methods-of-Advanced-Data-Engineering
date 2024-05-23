import os
from dags import airflow_dag
from logger import BaseLogger, ConsoleLogger
from utils import Config, convert_to_class_name
from etl_components import Extractor, CsvExtractor
from etl_components import TransformFactory, Transformer
from etl_components import Loader, SQLiteLoader

def main():
    
    try:
        console_logger: BaseLogger = ConsoleLogger()

        config = Config(
            logger      = console_logger, 
            file_path   = './config/pipeline_config.yaml'
        ).get()

        for dataset in config['datasets']:

            extractor: Extractor = CsvExtractor(
                logger      = console_logger,
                delimeter   = ";" if dataset['name'] == 'Solar_Flare_Data' else None
            )

            extractor.extract_data(
                extract_from    = dataset['source'],
                extract_to      = config['raw_path'],
                dataset_name    = dataset['name']
            )

            transformer: Transformer =  TransformFactory(logger = console_logger).get_transformer(
                transformer_name = convert_to_class_name(dataset['name'], splitter = '_', suffix = 'Transformer')
            )
            
            transformer.transform_data(
                read_from       = os.path.join(config['raw_path'], f"{dataset['name']}.csv"),
                write_to        = config['transformed_path'],
                dataset_name    = dataset['name']
            )
            
            loader: Loader = SQLiteLoader(logger = console_logger)

            loader.load_data(
                read_from       = config['transformed_path'],
                write_to        = config['sink'],
                database_name   = config['db_name']
            )
        
        console_logger.info("Pipeline execution completed.")

    except Exception as ex:
        console_logger.error(f"Error occured: {ex}")

if __name__ == "__main__":
    main()
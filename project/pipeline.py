import os
from dags import airflow_dag
from utils import read_config, logger
from etl_components import Extractor, CsvExtractor
from etl_components import TransformFactory

from etl_components import Loader, SQLiteLoader

def main():
    
    try:
        config = read_config('./config/pipeline_config.yaml')

        extract: Extractor = CsvExtractor()
        load: Loader = SQLiteLoader()

        for dataset in config['datasets']:

            extract.extract_data(
                extract_from    = dataset['source'],
                extract_to      = config['raw_path'],
                dataset_name    = dataset['name'],
                delimiter       = ";" if dataset['name'] == 'Solar_Flare_Data' else None
            )

            TransformFactory.transformers.get(dataset['name']).transform_data(
                read_from       = os.path.join(config['raw_path'], f"{dataset['name']}.csv"),
                write_to        = config['transformed_path'],
                dataset_name    = dataset['name']
            )

            load.load_data(
                read_from       = config['transformed_path'],
                write_to        = config['sink'],
                database_name   = config['db_name']
            )
        
        logger.info("Pipeline ezecution completed.")

    except Exception as ex:
        logger.error(f"Error occured: {ex}")

if __name__ == "__main__":
    main()
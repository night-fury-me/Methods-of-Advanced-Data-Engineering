from dags import airflow_dag
import os
from utils import read_config, logger
from etl_components import Extractor, CsvExtractor
from etl_components import (
    Transformer, 
    TemperatureDataTransformer,
    Co2ConcentrationDataTransformer,
    SeaLevelDataTransformer,
    SolarFlareDataTransformer
) 

from etl_components import Loader, SQLiteLoader

def main():
    config = read_config('./config/pipeline_config.yaml')

    extract: Extractor = CsvExtractor()
    tranform: Transformer = SolarFlareDataTransformer()
    load: Loader = SQLiteLoader()

    data_idx = 3

    extract.extract_data(
        extract_from=config['datasets'][data_idx]['source'],
        extract_to=config['raw_path'],
        dataset_name=config['datasets'][data_idx]['name'],
        delimiter=";"
    )

    tranform.transform_data(
        read_from=os.path.join(config['raw_path'], f"{config['datasets'][data_idx]['name']}.csv"),
        write_to=config['transformed_path'],
        dataset_name=config['datasets'][data_idx]['name']
    )

    load.load_data(
        read_from=config['transformed_path'],
        write_to=config['sink'],
        database_name='CombinedDataset.sqlite'
    )

    
if __name__ == "__main__":
    main()
import os
from datetime import datetime
from logger import BaseLogger, FileLogger
from utils import Config, convert_to_class_name
from ETL import Extractor, CsvExtractor
from ETL import TransformFactory, Transformer
from ETL import Loader, SQLiteLoader
from tasks import Task, TaskPipeline, PipelineQueue

def _extract(logger, config, dataset):
    extractor: Extractor = CsvExtractor(
        logger      = logger,
        delimeter   = ";" if dataset['name'] == 'Solar_Flare_Data' else None
    )

    extractor.extract_data(
        extract_from    = dataset['source'],
        extract_to      = config['raw_path'],
        dataset_name    = dataset['name']
    )

def _transform(logger, config, dataset):
    transformer: Transformer =  TransformFactory(logger = logger).get_transformer(
        transformer_name = convert_to_class_name(dataset['name'], splitter = '_', suffix = 'Transformer')
    )
    transformer.transform_data(
        read_from       = os.path.join(config['raw_path'], f"{dataset['name']}.csv"),
        write_to        = config['transformed_path'],
        dataset_name    = dataset['name']
    )

def _load(logger, config):
    loader: Loader = SQLiteLoader(logger = logger)

    loader.load_data(
        read_from       = config['transformed_path'],
        write_to        = config['sink'],
        database_name   = config['db_name']
    )


def main():
    
    try:
        log_file_path = datetime.now().strftime('logs/%Y%m%d_%H%M%S.log')
        file_logger: BaseLogger = FileLogger(log_file_path)

        config = Config(
            logger      = file_logger, 
            file_path   = './config/pipeline_config.yaml'
        ).get()


        pipeline_queue = PipelineQueue()

        for dataset in config['datasets']:
            extract = Task(
                name    = 'Extraction task',
                action  = (
                    lambda dataset  = dataset: 
                        _extract(file_logger, config, dataset)
                ),
                logger  = file_logger 
            )

            transform = Task(
                name    = 'Transform task',
                action  = (
                    lambda dataset = dataset:
                        _transform(file_logger, config, dataset)
                ),
                logger  = file_logger
            )

            load = Task(
                name    = 'Load task',
                action  = lambda: _load(file_logger, config),
                logger  = file_logger
            )
            
            pipeline = TaskPipeline(
                name    = f'Pipeline for {dataset['name']}',
                logger  = file_logger
            )

            (
                pipeline 
                    >> extract 
                        >> transform 
                            >> load
            )

            pipeline_queue.push(pipeline)

        pipeline_queue.run()

        file_logger.info("Pipeline execution completed.")

    except Exception as ex:
        file_logger.error(f"Error occured: {ex}")

if __name__ == "__main__":
    main()
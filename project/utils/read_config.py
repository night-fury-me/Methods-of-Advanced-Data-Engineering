import yaml
from utils import logger

def read_config(file_path):
    try:
        with open(file_path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info("Read the config file successfully.")
            return config
        
    except Exception as ex:
        logger.error(f"Error occured while reading config file: {ex}")
import yaml
import string
from logger import BaseLogger

class Config:
    def __init__(self, logger: BaseLogger, file_path: string) -> None:
        self.logger = logger
        self.file_path = file_path

    def get(self):
        try:
            with open(self.file_path, 'r') as f:
                config = yaml.safe_load(f)
                self.logger.info("Read the config file successfully.")
                return config
            
        except Exception as ex:
            self.logger.error(f"Error occured while reading config file: {ex}")
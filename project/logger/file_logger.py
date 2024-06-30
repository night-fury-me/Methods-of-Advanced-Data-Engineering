from .base_logger import BaseLogger
import logging

class FileLogger(BaseLogger):
    def __init__(self, filename: str) -> None:
        super().__init__()
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)
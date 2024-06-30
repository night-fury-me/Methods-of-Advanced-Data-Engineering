from .base_logger import BaseLogger
import logging

class ConsoleLogger(BaseLogger):
    def __init__(self) -> None:
        super().__init__()
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)

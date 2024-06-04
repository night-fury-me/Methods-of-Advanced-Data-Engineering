import logging
from .logger import Logger

class BaseLogger(Logger):
    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] - %(message)s'
        )

    def log(self, level: int, message: str) -> None:
        self.logger.log(level, message)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)

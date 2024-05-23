import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    '[%(asctime)s] [%(filename)s:%(lineno)d] [%(levelname)s] - %(message)s'
)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
from .transformer import Transformer
from .temperature_data_transformer import TemperatureDataTransformer
from .co2_concentration_data_transformer import Co2ConcentrationDataTransformer
from .sea_level_data_transformer import SeaLevelDataTransformer
from .solar_flare_data_transformer import SolarFlareDataTransformer
from logger import BaseLogger
from typing import Type
import string

class TransformFactory:

    def __init__(self, logger: BaseLogger) -> None:
        self.transformers = {
            TemperatureDataTransformer.__name__      : TemperatureDataTransformer(logger = logger),
            Co2ConcentrationDataTransformer.__name__ : Co2ConcentrationDataTransformer(logger = logger),
            SeaLevelDataTransformer.__name__         : SeaLevelDataTransformer(logger = logger),
            SolarFlareDataTransformer.__name__       : SolarFlareDataTransformer(logger = logger)
        }

    def get_transformer(self, transformer_name: string):
        return self.transformers.get(transformer_name)
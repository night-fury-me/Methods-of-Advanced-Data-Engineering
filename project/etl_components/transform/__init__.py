from .transformer import Transformer
from .temperature_data_transformer import TemperatureDataTransformer
from .co2_concentration_data_transformer import Co2ConcentrationDataTransformer
from .sea_level_data_transformer import SeaLevelDataTransformer
from .solar_flare_data_transformer import SolarFlareDataTransformer

class TransformFactory:

    transformers = {
        'Temperature_Data' : TemperatureDataTransformer(),
        'Co2_Concentration_Data': Co2ConcentrationDataTransformer(),
        'Sea_Level_Data': SeaLevelDataTransformer(),
        'Solar_Flare_Data': SolarFlareDataTransformer()
    }
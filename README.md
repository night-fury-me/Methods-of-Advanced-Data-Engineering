# Exercise Badges

![](https://byob.yarr.is/night-fury-me/Methods-of-Advanced-Data-Engineering/score_ex1) ![](https://byob.yarr.is/night-fury-me/Methods-of-Advanced-Data-Engineering/score_ex2) ![](https://byob.yarr.is/night-fury-me/Methods-of-Advanced-Data-Engineering/score_ex3) ![](https://byob.yarr.is/night-fury-me/Methods-of-Advanced-Data-Engineering/score_ex4) ![](https://byob.yarr.is/night-fury-me/Methods-of-Advanced-Data-Engineering/score_ex5)

# Influence of Solar Activity on Earth's Climate

<img src="project/data-report/solar-activity-climate-change_02.jpg" alt="Project Logo" width="100%">
Image Reference: 

[earth.com](https://www.earth.com/news/a-massive-solar-flare-struck-earth-on-monday-but-what-does-this-mean/)


### Introduction
The project aims to explore the possible connection between solar activity - like solar flares, and climate change on
Earth. Through the statistical analysis of historical data, our goal is to uncover whether there exists a clear relationship
between solar events and the observable shift in global climate patterns. This investigation holds significant importance
as it provides insights essential for refining climate models and improving our capacity to forecast and address the
consequences of climate change.

### Research Question

`Is there any relationship between solar activity (Solar Flares) and climate change on Earth?`

### Project Structure

```
project
├── ETL
│   ├── __init__.py
│   ├── extract
│   │   ├── __init__.py
│   │   ├── csv_extractor.py
│   │   ├── extractor.py
│   ├── load
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── sqlite_loader.py
│   └── transform
│       ├── __init__.py
│       ├── co2_concentration_data_transformer.py
│       ├── sea_level_data_transformer.py
│       ├── solar_flare_data_transformer.py
│       ├── temperature_data_transformer.py
│       └── transformer.py
├── config
│   └── pipeline_config.yaml
├── data
│   ├── raw
│   │   ├── Co2_Concentration_Data.csv
│   │   ├── Solar_Flare_Data.csv
│   │   └── Temperature_Data.csv
│   ├── sink
│   │   └── CombinedDataset.sqlite
│   └── transformed
│       ├── Co2_Concentration_Data.csv
│       ├── Solar_Flare_Data.csv
│       └── Temperature_Data.csv
├── data-analysis
│   ├── data-analysis.ipynb
│   └── plots
├── data-report
├── logger
│   ├── __init__.py
│   ├── base_logger.py
│   ├── console_logger.py
│   ├── file_logger.py
│   ├── logger.py
├── logs
│   └── 20240701_043653.log
├── notebooks
├── tasks
│   ├── __init__.py
│   └── task.py
├── tests
│   ├── __init__.py
│   ├── mock
│   │   ├── __init__.py
│   │   ├── data
│   │   │   ├── __init__.py
│   │   │   ├── co2_concentration_mock_data.py
│   │   │   ├── raw
│   │   │   │   ├── CO2_Concentration_Mock_Data.csv
│   │   │   │   ├── Data_For_Pipeline_Test.csv
│   │   │   │   ├── Solar_Flare_Mock_Data.csv
│   │   │   │   └── Temperature_Change_Mock_Data.csv
│   │   │   ├── sink
│   │   │   │   └── dataset.sqlite
│   │   │   ├── solar_flare_mock_data.py
│   │   │   ├── temperature_change_mock_data.py
│   │   │   └── transformed
│   │   │       ├── CO2_Concentration_Mock_Data.csv
│   │   │       ├── Data_For_Pipeline_Test.csv
│   │   │       ├── Solar_Flare_Mock_Data.csv
│   │   │       └── Temperature_Change_Mock_Data.csv
│   │   └── mock_logger.py
│   ├── test_system.py
│   └── test_transform.py
├── utils
│   ├── __init__.py
│   ├── config.py
│   └── converters.py
├── analysis-report.pdf
├── data-report.pdf
├── pipeline.py
├── pipeline.sh
├── tests.py
├── tests.sh
├── project-plan.md
└── requirements.txt
```



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
│   ├── sink
│   └── transformed
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
│   │   │   ├── solar_flare_mock_data.py
│   │   │   ├── temperature_change_mock_data.py
│   │   │   ├── raw
│   │   │   ├── sink
│   │   │   └── transformed
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

### Installation

### Using conda

To install necessary dependencies using conda, execute the following command after cloning the repository:

```bash
conda env create -f environment.yml
```

This command will create a conda environment named `made-env` (or any other specified name in your `environment.yml` file) and install all required packages.

Using pip

If you prefer using pip, you can install the dependencies listed in `requirements.txt`. Make sure you have Python and pip installed, then run:

```bash
pip install -r requirements.txt
```

### Running the Data Pipeline

You can run the data pipeline using either `pipeline.sh` or `pipeline.py`:

```bash
cd project
chmod +x pipeline.sh
./pipeline.sh
OR
python pipeline.py
```

### Running Unit Tests

To run unit tests for the data pipeline, use either `tests.sh` or `tests.py`:

```bash
cd project
chmod +x tests.sh
./tests.sh
OR
python tests.py
```

### Continuous Integration with GitHub Actions

Whenever a commit is pushed to this repository, the unit tests for the data pipeline will be automatically triggered using GitHub Actions. The status of the test run will be notified to the Slack channel `#made-ci-cd` as shown in the image below:

<img src="project/data-report/slack-webhook.png" alt="slack-webhook.png" width="100%">

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.



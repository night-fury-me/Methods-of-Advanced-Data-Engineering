import os
import pandas as pd
import numpy as np

file_path = 'tests/mock/data/raw/CO2_Concentration_Mock_Data.csv'

parent_directory = os.path.dirname(file_path)
os.makedirs(parent_directory, exist_ok=True)

columns = ['Unnamed: 0', 'ObjectId', 'Country', 'ISO2', 'ISO3', 'Indicator', 'Unit', 'Source', 'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor', 'Date', 'Value']

data = {
    'Unnamed: 0': range(1, 11),
    'ObjectId': np.random.randint(1000, 2000, size=10),
    'Country': ['Country A', 'Country B', 'Country C', 'Country D', 'Country E', 'Country F', 'Country G', 'Country H', 'Country I', 'Country J'],
    'ISO2': ['CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ'],
    'ISO3': ['CTA', 'CTB', 'CTC', 'CTD', 'CTE', 'CTF', 'CTG', 'CTH', 'CTI', 'CTJ'],
    'Indicator': ['Indicator 1', 'Indicator 2', 'Indicator 3', 'Indicator 4', 'Indicator 5', 'Indicator 6', 'Indicator 7', 'Indicator 8', 'Indicator 9', 'Indicator 10'],
    'Unit': ['Unit 1', 'Unit 2', 'Unit 3', 'Unit 4', 'Unit 5', 'Unit 6', 'Unit 7', 'Unit 8', 'Unit 9', 'Unit 10'],
    'Source': ['Source 1', 'Source 2', 'Source 3', 'Source 4', 'Source 5', 'Source 6', 'Source 7', 'Source 8', 'Source 9', 'Source 10'],
    'CTS_Code': np.random.randint(100, 200, size=10),
    'CTS_Name': ['CTS Name 1', 'CTS Name 2', 'CTS Name 3', 'CTS Name 4', 'CTS Name 5', 'CTS Name 6', 'CTS Name 7', 'CTS Name 8', 'CTS Name 9', 'CTS Name 10'],
    'CTS_Full_Descriptor': ['Descriptor 1', 'Descriptor 2', 'Descriptor 3', 'Descriptor 4', 'Descriptor 5', 'Descriptor 6', 'Descriptor 7', 'Descriptor 8', 'Descriptor 9', 'Descriptor 10'],
    'Date': pd.date_range(start='1958-01-01', periods=10, freq='ME').strftime('%Y') + 'M' + pd.date_range(start='1958-01-01', periods=10, freq='ME').strftime('%m'),
    'Value': np.random.rand(10) * 100
}

CO2_Concentration_Mock_Data = pd.DataFrame(data, columns=columns)
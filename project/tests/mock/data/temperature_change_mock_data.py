import pandas as pd
import numpy as np

columns = ['ObjectId', 'Country', 'ISO2', 'ISO3', 'Indicator', 'Unit', 'Source', 
           'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor'] + [f'F{year}' for year in range(1961, 2023)]

data = {
    'ObjectId': np.arange(1, 11),
    'Country': ['Country1', 'Country2', 'Country3', 'Country4', 'Country5', 
                'Country6', 'Country7', 'Country8', 'Country9', 'Country10'],
    'ISO2': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'],
    'ISO3': ['CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6', 'CO7', 'CO8', 'CO9', 'CO10'],
    'Indicator': ['Temperature Change']*10,
    'Unit': ['°C']*10,
    'Source': ['Source1']*10,
    'CTS_Code': ['Code1']*10,
    'CTS_Name': ['Name1']*10,
    'CTS_Full_Descriptor': ['Full Descriptor1']*10
}

for year in range(1961, 2023):
    data[f'F{year}'] = np.random.uniform(-1, 1, 10)


Temperature_Change_Mock_Data = pd.DataFrame(data, columns=columns)

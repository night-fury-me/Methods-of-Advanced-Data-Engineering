import pandas as pd
from datetime import datetime, timedelta

base_time = datetime(2024, 1, 1, 0, 0)
date_times = [base_time + timedelta(hours=i*2) for i in range(10)]  # every 2 hours for variety
date_times_str = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in date_times]

columns = ['Unnamed: 0', 'FlareNumber', 'T_REC', 'NOAA_AR', 'QUALITY', 'Longitude', 'Latitude', 'TOTUSJH', 'TOTBSQ', 'TOTPOT', 'TOTUSJZ', 'ABSNJZH', 'SAVNCPP', 'USFLUX', 'AREA_ACR', 'TOTFZ', 'MEANPOT', 'R_VALUE', 'EPSZ', 'SHRGT45', 'MEANSHR', 'MEANGAM', 'MEANGBT', 'MEANGBZ', 'MEANGBH', 'MEANJZH', 'TOTFY', 'MEANJZD', 'MEANALP', 'TOTFX', 'EPSY', 'EPSX']

data = {
    'Unnamed: 0': range(10),
    'FlareNumber': [f'F{i+1}' for i in range(10)],
    'T_REC': date_times_str,
    'NOAA_AR': range(1000, 1010),
    'QUALITY': [1]*10,
    'Longitude': [i*10 for i in range(10)],
    'Latitude': [i*5 for i in range(10)],
    'TOTUSJH': [100 + i for i in range(10)],
    'TOTBSQ': [200 + i for i in range(10)],
    'TOTPOT': [300 + i for i in range(10)],
    'TOTUSJZ': [400 + i for i in range(10)],
    'ABSNJZH': [500 + i for i in range(10)],
    'SAVNCPP': [600 + i for i in range(10)],
    'USFLUX': [700 + i for i in range(10)],
    'AREA_ACR': [800 + i for i in range(10)],
    'TOTFZ': [900 + i for i in range(10)],
    'MEANPOT': [1000 + i for i in range(10)],
    'R_VALUE': [1100 + i for i in range(10)],
    'EPSZ': [1200 + i for i in range(10)],
    'SHRGT45': [1300 + i for i in range(10)],
    'MEANSHR': [1400 + i for i in range(10)],
    'MEANGAM': [1500 + i for i in range(10)],
    'MEANGBT': [1600 + i for i in range(10)],
    'MEANGBZ': [1700 + i for i in range(10)],
    'MEANGBH': [1800 + i for i in range(10)],
    'MEANJZH': [1900 + i for i in range(10)],
    'TOTFY': [2000 + i for i in range(10)],
    'MEANJZD': [2100 + i for i in range(10)],
    'MEANALP': [2200 + i for i in range(10)],
    'TOTFX': [2300 + i for i in range(10)],
    'EPSY': [2400 + i for i in range(10)],
    'EPSX': [2500 + i for i in range(10)]
}

Solar_Flare_Mock_Data = pd.DataFrame(data, columns=columns)
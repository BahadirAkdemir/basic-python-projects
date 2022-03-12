import pandas as pd

data = pd.read_csv('read_csv/weather_data.csv')
print(data["temp"].mean())
print(data["temp"].max())
print(data[data.temp==data.temp.max()])
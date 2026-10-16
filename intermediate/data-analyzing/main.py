import csv
import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data) # pandas dataframe
# print(type(data["temp"])) # pandas series
temp_list = data["temp"].to_list()
mean_temp = data["temp"].mean()
# print(mean_temp)
# print(data["temp"].max())
monday = data[data["day"] == "Monday"]
celsius_temp = monday["temp"]
print("fa*******************")
fa_temp = (celsius_temp * 1.8) + 32
print(fa_temp)


import csv
# import pandas as pd
with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temp_list =[]
    print(data)
    for row in data:
        if row[1].isalpha() != True:
            temp_list.append(int(row[1]))
    print(temp_list)
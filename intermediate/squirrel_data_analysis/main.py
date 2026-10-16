import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20261016.csv")

color_counts = data["Primary Fur Color"].value_counts() # count the number of unique values 
print(type(color_counts))
print("*******************************0")
data_color_dict = {} # empty dict
data_color_ct = {
    "Gray": 55,
    "Black": 30,
    "Red": 15
}

for color in  color_counts.keys():
    # print(color)
    color_count = color_counts.get(color, 0)
    print(color_count)
    data_color_dict[color] = color_count

new_dataframe = pd.DataFrame(
    list(data_color_dict.items()),
    columns=["Primary_Fur_Color", "Count"]
)
# new_dataframe.to_csv("new_squirrel_data1.csv", index = True)
new_dataframe.to_csv("new_squirrel_data2.csv", index = False)


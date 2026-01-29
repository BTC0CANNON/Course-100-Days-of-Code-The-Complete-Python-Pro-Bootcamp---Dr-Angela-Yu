# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# # print(temp_list)

"""Get the average temp before Panda"""
# total = 0
# for temp in temp_list:
#     total += temp
#
# temp_average = total / len(temp_list)

"""OR"""
# temp_average = sum(temp_list) / len(temp_list)
# print(temp_average)

"""After panda"""
# print(data["temp"].mean())

"""Max"""
# print(data["temp"].max())

"""Get Data in Columns"""
# print(data["condition"])
# print(data.condition)

"""Get Data in Rows"""
# print(data[data.day == "Monday"])

"""Day with max temp"""
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

"""convert to fahrenheit"""
# print(monday.temp * 1.8 + 32)

"""Create a dataframe from scratch"""
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

"""Squirrel Census Data Analysis"""

"""My Code"""
data =  pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data["Primary Fur Color"]
color_gray = 0
color_red = 0
color_black = 0
for color in fur_colors:
    if color == "Gray":
        color_gray += 1
    if color == "Cinnamon":
        color_red += 1
    if color == "Black":
        color_black += 1

color_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [color_gray, color_red, color_black]
}
fur_color_data = pandas.DataFrame(color_dict)
fur_color_data.to_csv("fur_color_data.csv")

"""Angela's Code"""
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

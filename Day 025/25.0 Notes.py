# import csv
#
# with open("weather_data.csv") as file:
#     reader = csv.reader(file)
#     file_list = list(reader)
#
# temperatures = []
#
# for day, temperature, weather in file_list[1:]:
#     temperatures.append(int(temperature))
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(sum(temp_list)/len(temp_list))
print(data["temp"].mean())

print(data["temp"].max())

print(data.temp)

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp_f = monday.temp * 9/5 + 32
print(monday_temp_f)

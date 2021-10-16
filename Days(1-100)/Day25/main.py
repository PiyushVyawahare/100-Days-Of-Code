# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


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

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
#
# # temp_list = data["temp"].to_list()
# # print(f"Average temperature = {sum(temp_list)/len(temp_list)}")
#
# print(f'Average temperature = {data["temp"].mean()}')
# print(f'Max temperature = {data.temp.max()}')
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in row
# print(data[data.day == "Monday"])
#
# # Get data in row for highest temperature
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((int(monday.temp)*9/5)+32)

# create dataframe from scratch

data_dict = {
    "students": ["Piyush", "Varun", "Pranav"],
    "scores": [95, 93, 78]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

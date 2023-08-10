# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     day = []
#     condition = []
#     header = False
#     for row in data:
#         if header:
#             day.append(row[0])
#             temperature.append(int(row[1]))
#             condition.append(row[2])
#         header = True
#         print(row)
#
#     print(day)
#     print(temperature)
#     print(condition)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
#
# temperature = data["temp"]
# print(temperature)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

print(data["temp"].mean())

print(data["temp"].max())

#get data in columns
print(data["condition"])
#in the bg, pandas converts the columns to attributes respectfully to the 1st row in the column
print(data.condition)

#get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

sunday = data[data.day == "Sunday"]
print(sunday.condition)

print(sunday.temp)
sunday_temp_fahrenheit = 32 + int(sunday.temp) * 9 / 5
print(sunday_temp_fahrenheit)

#create a dataframe from scratch
scratch_dict = {
    "students" : ["Amy", "John", "Tommy"],
    "scores" : [76, 55, 90]
}

scratch = pandas.DataFrame(scratch_dict)
print(scratch)

scratch.to_csv("new_data.csv")

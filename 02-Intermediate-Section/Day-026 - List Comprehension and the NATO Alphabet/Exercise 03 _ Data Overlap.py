with open("file1.txt") as data_1:
  list_1 = data_1.readlines()

with open("file2.txt") as data_2:
  list_2 = data_2.readlines()

result = [int(item.strip("\n")) for item in list_1 if item in list_2]
# Write your code above 👆

print(result)

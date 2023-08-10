#Write your code below this row 👇
total_even = 0

for number in range(1, 101):
    if number % 2 == 0:
        total_even += number

print(total_even)

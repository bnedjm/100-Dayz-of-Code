############DEBUGGING#####################

# # Describe Problem
def my_function():
  #for i in range(1, 20): the range function ommits the upper bound
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6) randint includes both bounds and lists start count from 0
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
#elif year > 1994: we had no condition for = 1994
elif year >= 1994:
  print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?")) #we need to cast the input to int from string / stdr input
if age > 18:
  print(f"You can drive at age {age}.") #tab the print to fit the if

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) #used == instead of = to express assignement
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  #b_list.append(new_item)
    b_list.append(new_item) #tab the statement so that it will be included in the if condition
  print(b_list)

mutate([1,2,3,5,8,13])

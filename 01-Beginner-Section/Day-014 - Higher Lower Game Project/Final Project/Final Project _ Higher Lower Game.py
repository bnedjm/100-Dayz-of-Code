#import all
from art import logo
from art import vs
from game_data import data
from random import randint
from replit import clear

#function to generate a random option from the database
def generate_option(data, placebo):
  idx = randint(0 ,len(data))
  if data[idx] in placebo:
    return generate_option(data, placebo)
  else:
    placebo.append(data[idx])
    return data[idx]

    
#function to compare options
def check_if_correct(option_1, option_2):
  if option_1["follower_count"] > option_2["follower_count"]:
    return "A"
  elif option_1["follower_count"] < option_2["follower_count"]:
    return "B"


#game function 

def game():
  #generate options
  placebo = [data[0]]
  option_1 = generate_option(data, placebo)
  option_2 = generate_option(data, placebo)
  
  score = 0
  wrong_answer = False 
  
  while not wrong_answer:
    clear()
    print(logo)
    
    if score != 0:
      print(f"You are right! current score is :\t{score}")
    
    guess = input(f"Compare A: {option_1['name']}, a {option_1['description']} from {option_1['country']}.\n{vs}\nAgainst B: {option_2['name']}, a {option_2['description']} from {option_2['country']}.\nWho has more followers? Type 'A' or 'B':\t")
    
    #game conditionals
    if guess == "A" and guess == check_if_correct(option_1, option_2):
      option_2 = generate_option(data, placebo)
      score += 1
    elif guess == "B" and guess == check_if_correct(option_1, option_2):
      option_1 = option_2
      option_2 = generate_option(data, placebo)
      score += 1
    elif guess != check_if_correct(option_1, option_2):
      wrong_answer = True
      clear()

  print(f"Sorry, that is wrong! Final score:\t{score}")
  
  replay = input("Do you want to play again? Type 'yes' or 'no'.\n")
  
  if replay == "yes":
    game()

game()

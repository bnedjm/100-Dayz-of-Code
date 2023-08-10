from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

#Function to check user's guess against actual answer.
def check_if_correct(guess, target, chances):
  if guess > target:
    print("Too high.")
    if chances != 1:
      print("Guess again.")
    return chances - 1
  elif guess < target:
    print("Too low.")
    if chances != 1:
      print("Guess again.")
    return chances - 1
  else:
    print(f"You got it! The answer was {target}.")
  
#Make function to set difficulty.
def set_difficulty():
  dif = input("Choose a difficulty. Type 'easy' or 'hard':\t")
  if dif == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL

def game():
  #Choosing a random number between 1 and 100.
  print(logo)
  print('''
  Welcome to the Number Guessing Game!
  I am thinking of a number between 1 and 100.''')
  target = randint(1, 100)
  
  #Let the user guess a number.
  #Repeat the guessing functionality if they get it wrong. 
  chances = set_difficulty()
  guess = 0
  while guess != target:
    guess = int(input(f"You have {chances} attempts remaining to guess the number.\nMake a guess:\t")) 
    
    #Track the number of turns and reduce by 1 if they get it wrong.
    chances = check_if_correct(guess = guess, target = target, chances = chances)
    if chances == 0:
      print("You have run out of guesses, you lose.")
      return
   
game()

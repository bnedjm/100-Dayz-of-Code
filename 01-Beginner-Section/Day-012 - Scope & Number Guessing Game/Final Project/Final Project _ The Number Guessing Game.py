#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)
print('''
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.''')

import random
target = random.randint(1, 100)

invalid_input = True
while invalid_input:
  dif = input("Choose a difficulty. Type 'easy' or 'hard':\t")
  invalid_input = False
  if dif == "easy":
    chances = 10
  elif dif == "hard":
    chances = 5
  else:
    print("Invalid input, please try again!")
    invalid_input = True

right = False
while not right:
  guess = int(input(f"You have {chances} attempts remaining to guess the number.\nMake a guess:\t"))
  if guess > target:
    print("Too high.\nGuess again.")
    chances -= 1
  elif guess < target:
    print("Too low.\nGuess again.")
    chances -= 1
  else:
    print(f"You got it! The answer was {target}.")
    right = True

  if chances == 0:
    print("You have run out of guesses, you lose.")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choices = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if choice >= 3 or choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(choices[choice])
  
  print("Computer chose:\n")
  Comp_choice = random.randint(0,2)
  print(choices[Comp_choice])

  if choice == 0 and Comp_choice == 2:
    print("You Win!")
  elif choice > Comp_choice:
    print("You Win!")
  elif choice < Comp_choice:
    print("You Loose!")
  elif choice == Comp_choice:
    print("It is a Draw!")

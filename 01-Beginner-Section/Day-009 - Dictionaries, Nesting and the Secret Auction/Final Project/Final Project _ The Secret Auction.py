from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
repeat = True

def find_winner(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    if bid_record[bidder] > highest_bid:
      highest_bid = bid_record[bidder]
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
while repeat:
  
  name = input("What is your name?\t")
  bid = int(input("What is your bid? $"))
  bids[name] = bid

  more_bidders = input("Are there any more bidders? type 'yes' or ' no'.\n").lower() 
  if more_bidders == "no":
    clear()
    repeat = False
  elif more_bidders == "yes":
    clear()

find_winner(bids)

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

ttl_bill = input("Welcome to the tip calculator!\nWhat was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
ppl = input("How many people to split the bill? ")

ttl_bill = float(ttl_bill)
tip = int(tip)
ppl = int(ppl)

ind_bill = (ttl_bill / ppl) * (1 + tip / 100)
#ind_bill = round(ind_bill,2)
ind_bill = "{:.2f}".format(ind_bill)

print(f"Each person shoud pay: ${ind_bill}")

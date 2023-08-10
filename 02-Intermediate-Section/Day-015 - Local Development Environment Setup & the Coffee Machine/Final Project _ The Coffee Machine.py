MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
# TODO: 1. a. Check the user’s input to decide what to do next.
# choice = input("What would you like? (espresso/latte/cappuccino):\t")


# TODO: 1. b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 2. a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
def turned_on(choice):
    on = True
    if choice == "off":
        on = False
    return on


# associate the variable "on" to the operational loop

# TODO: 3. Print report.
# TODO: 3. a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
def report():
    for idx in resources:
        if idx == "milk" or idx == "water":
            print(f"{idx.title()} : {resources[idx]}ml")
        elif idx == "coffee":
            print(f"{idx.title()} : {resources[idx]}g")
        elif idx == "money":  # to recheck
            print(f"{idx.title()} : ${resources[idx]}")


# this should be defined as a function

# TODO: 4. Check resources sufficient?
# TODO: 4. a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# TODO: 4. b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
# TODO: 4. c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resources(choice):
    sufficient_resources = True
    choice_ing = MENU[choice]["ingredients"]
    for ingredient in choice_ing:
        if resources[ingredient] < choice_ing[ingredient]:
            sufficient_resources = False
            print(f"Sorry there is not enough {ingredient}.")
            return sufficient_resources
    return sufficient_resources


# this should be defined as a function

# TODO: 5. Process coins.
# TODO: 5. a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# TODO: 5. b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# TODO: 5. c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def process_coins():
    credit = 0
    print("Please insert coins.")
    quarters = int(input("how many quarters?:\t"))
    credit += quarters * 0.25
    dimes = int(input("how many dimes?:\t"))
    credit += dimes * 0.10
    nickles = int(input("how many nickles?:\t"))
    credit += nickles * 0.05
    pennies = int(input("how many pennies?:\t"))
    credit += pennies * 0.01
    return credit


# this should be defined as a function

# TODO: 6. Check transaction successful?
# TODO: 6. a.  Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
# TODO: 6. b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# TODO: 6. c. If the user has inserted too much money, the machine should offer change.
def check_credit(enough_resources, choice):
    sufficient_credit = True
    if enough_resources:
        credit = process_coins()
        if credit < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            sufficient_credit = False
        elif credit >= MENU[choice]["cost"]:
            if credit > MENU[choice]["cost"]:
                change = credit - MENU[choice]["cost"]
                print(f"Here is {change} in change.")
    return sufficient_credit
    # this should be defined as a function


# TODO: 7. Make Coffee.
# TODO: 7. a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
# TODO: 7. b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

def make_coffee(enough_resources, enough_credit, choice):
    if enough_resources and enough_credit:
        for resource in MENU[choice]["ingredients"]:
            if resource == "water" or resource == "milk" or resource == "coffee":
                resources[resource] -= MENU[choice]["ingredients"][resource]

        resources["money"] += MENU[choice]["cost"]
        print(f"Here is your {choice.title()}. Enjoy!")


def coffee_machine():
    choice = input("What would you like? (espresso/latte/cappuccino):\t").lower()
    keywords = ["off", "espresso", "latte", "cappuccino", "report"]
    credit_ = 0
    if choice not in keywords:
        coffee_machine()
    elif turned_on(choice) and choice != "report":
        enough_resources = check_resources(choice)
        enough_credit = check_credit(enough_resources, choice)
        make_coffee(enough_resources, enough_credit, choice)
        coffee_machine()
    elif not turned_on(choice):
        return
    elif choice == "report":
        report()
        coffee_machine()


resources["money"] = 0
coffee_machine()

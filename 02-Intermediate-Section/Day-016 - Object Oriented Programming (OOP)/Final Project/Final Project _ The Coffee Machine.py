from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
# TODO: 1. a. Check the user’s input to decide what to do next.
# TODO: 1. b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
MENU = Menu()
COFFEE_MAKER = CoffeeMaker()
MONEY_MACHINE = MoneyMachine()

turned_on = True
while turned_on:
    choice = input(f"What would you like? ({MENU.get_items()}):\t")

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 2. a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
    if choice == "off":
        turned_on = False

# TODO: 3. Print report.
# TODO: 3. a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    elif choice == "report":
        COFFEE_MAKER.report()
        MONEY_MACHINE.report()

# TODO: 4. Check resources sufficient?
# TODO: 4. a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# TODO: 4. b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
# TODO: 4. c. The same should happen if another resource is depleted, e.g. milk or coffee.
    elif MENU.find_drink(choice) is not None:
        order = MENU.find_drink(choice)
        if COFFEE_MAKER.is_resource_sufficient(order):


# TODO: 5. Process coins.
# TODO: 5. a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# TODO: 5. b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# TODO: 5. c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO: 6. Check transaction successful?
# TODO: 6. a.  Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
# TODO: 6. b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# TODO: 6. c. If the user has inserted too much money, the machine should offer change.
            if MONEY_MACHINE.make_payment(order.cost):

# TODO: 7. Make Coffee.
# TODO: 7. a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
# TODO: 7. b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
                COFFEE_MAKER.make_coffee(order)

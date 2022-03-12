
from requirements import coffees,coins,stock 

while True:
    print("Welcome to Coffee Machine, Which one do you want to buy? (cappuccino,latte,espresso)")
    user_input = input()
    if stock["milk"]>=coffees[user_input]["milk"] and stock["coffee"]>=coffees[user_input]["coffee"] and stock["water"]>=coffees[user_input]["water"]:
        penny = int(input("How many pennies do you have?"))
        nickel = int(input("How many nickels do you have?"))
        dime = int(input("How many dimes do you have?"))
        quarter = int(input("How many quarters do you have?"))
        if (penny*coins["penny"]+nickel*coins["nickel"]+dime*coins["dime"]+quarter*coins["quarter"])>= coffees[user_input]["price"]:
            print("Please take your drink")
            stock["milk"]-=coffees[user_input]["milk"]
            stock["coffee"]-=coffees[user_input]["coffee"]
            stock["water"]-=coffees[user_input]["water"]
            change = (penny*coins["penny"]+nickel*coins["nickel"]+dime*coins["dime"]+quarter*coins["quarter"])- coffees[user_input]["price"]
            print(f"Your change is {change}")
    else:
        print("Sorry, we are out of stock")
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0,
}
def is_transaction_successful(money_received, drink_cost):
    if drink_cost > money_received:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        return True

def process_coins():
    """Return the total calculated from coins inserted"""
    print("Please insert Coins. ")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_resource_sufficient(ordered_ingredients):
    """Returns True if oreder can be made, else returns False."""
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def make_coffee(drink_name, ordered_ingredient):
    """Deduct the required ingredients from the resources"""
    for item in ordered_ingredient:
        resources[item] -= ordered_ingredient[item]
    print(f"Here's your Coffee, {drink_name}☕")

while True:
    choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]

        flag = is_resource_sufficient(drink["ingredients"])
        if flag:
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
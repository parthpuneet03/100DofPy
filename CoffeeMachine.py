flavours = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 18
        },
        "cost": 3.0
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}


def resource_checker(selected_flav):
    item = flavours[selected_flav]
    ing_needed = item["ingredients"]
    if (ing_needed['water'] <= resources['water'] and ing_needed['milk'] <= resources['milk'] and ing_needed['coffee']
            <= resources['coffee']):
        return 1
    elif ing_needed['water'] > resources['water']:
        return "water"
    elif ing_needed['coffee'] > resources['coffee']:
        return "coffee"
    elif ing_needed['milk'] < resources['milk']:
        return "milk"


def pay_coins():
    penny = int(input("Enter the number of pennies(0.01$): "))
    nickel = int(input("Enter the number of nickels(0.05$): "))
    dime = int(input("Enter the number of dimes(0.10$): "))
    quarter = int(input("Enter the number of quarters(0.25$): "))
    money_paid = (penny * coins["penny"] + nickel * coins["nickel"] + dime * coins["dime"] + quarter * coins["quarter"])
    return money_paid


def update_inventory(selected_flavour):
    STUFFinFlav = flavours[selected_flavour]
    ingredients = STUFFinFlav["ingredients"]
    price = STUFFinFlav['cost']
    resources['water'] -= ingredients['water']
    resources['milk'] -= ingredients['milk']
    resources['coffee'] -= ingredients['coffee']
    resources['money'] += price


# ToDo:1. prompt user to ask what flavours would they like and take input for espresso, latte or cappuccino
# TODO:2. Show the report of its resources present if input==report
# TODO:3. check whether the flavoured you have asked has enough resources available for it to be made
# TODO:4. asks user to insert money in form of coin
# TODO:5. def a function that checks whether the amt entered is equal to greater than the cost req for selected flavour
# TODO:6. after coffee is made, deduct the resources according to the ingredients  used up in the coffee machine

cont = True
while cont:
    user_choice = input('''What would you like to have? 
(Espresso, Latte, Cappuccino)
or type "off" to turn off the machine \n''').lower()
    if user_choice == "report":
        for _ in resources:
            print(f"{_}: {resources[_]}")
    elif user_choice == "off":
        print("Turning Coffee Machine Off")
        cont = False
    else:
        if resource_checker(user_choice) == 1:
            selected_flav = flavours[user_choice]
            cost_of_flav = selected_flav["cost"]
            cost=selected_flav["cost"]
            print(f'For {user_choice}, please pay ${cost}')
            amt_paid = pay_coins()
            change = round((amt_paid - cost_of_flav), 2)
            if change == 0:
                print(f"getting your {user_choice}... \n")
                update_inventory(user_choice)
            elif change > 0:
                print(f"getting your {user_choice}... collect your change: ${change}\n")
                update_inventory(user_choice)
            else:
                print("Sorry that's not enough money. Money refunded.\n")
        else:
            print(f"Sorry there isn't enough {resource_checker(user_choice)}")



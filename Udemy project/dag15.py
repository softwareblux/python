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


    
    
    


on = True
money = 0
while on:
    
    what = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if what == "report":
        print(f"{resources['coffee']} grams of coffee")
        print(f"{resources['milk']}ml of milk")
        print(f"{resources['water']}ml of water")
        print(f"${money}")
    
    elif what == "espresso":
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        
        # print(resources["coffee"])
        # print(resources["water"])
        
        if resources["coffee"] < 0:
            on = False
            print("Not enough coffee")
        if resources["water"] < 0:
            on = False
            print("Not enough water")

        else:
            quarters = int(input("How many quarters? "))*0.25
            dimes = int(input("How many dimes? "))*0.1
            nickles = int(input("How many nickles? "))*0.05
            pennies = int(input("How many pennies? "))*0.01
            summen = quarters + dimes + nickles + pennies
            if summen > 1.5:
                print(f"${round(summen,2)-1.5} money back")
                print("Enjoy your coffee")
                money+=1.5
            if summen == 1.5:
                print("Enjoy your coffee")
                money+=1.5
            if summen < 1.5:
                print(f"You need ${1.5-round(summen,2)}")
            
        
        

    elif what == "latte":
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        
        # print(resources["coffee"])
        # print(resources["water"])

        if resources["coffee"] < 0:
            on = False
            print("Not enough coffee")
        if resources["water"] < 0:
            on = False
            print("Not enough water")
        if resources["milk"] < 0:
            on = False
            print("Not enough milk")

        else:
            quarters = int(input("How many quarters? "))*0.25
            dimes = int(input("How many dimes? "))*0.1
            nickles = int(input("How many nickles? "))*0.05
            pennies = int(input("How many pennies? "))*0.01
            summen = quarters + dimes + nickles + pennies
            if summen > 2.5:
                print(f"${round(summen,2)-2.5} money back")
                print("Enjoy your coffee")
                money+=2.5
            if summen == 2.5:
                print("Enjoy your coffee")
                money+=2.5
            if summen < 2.5:
                print(f"You need ${2.5-round(summen,2)}")


    elif what == "cappuccino":
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        
        # print(resources["coffee"])
        # print(resources["water"])
        if resources["coffee"] < 0:
            on = False
            print("Not enough coffee")
        if resources["water"] < 0:
            on = False
            print("Not enough water")
        if resources["milk"] < 0:
            on = False
            print("Not enough milk")

        else:
            quarters = int(input("How many quarters? "))*0.25
            dimes = int(input("How many dimes? "))*0.1
            nickles = int(input("How many nickles? "))*0.05
            pennies = int(input("How many pennies? "))*0.01
            summen = quarters + dimes + nickles + pennies
            if summen > 3:
                print(f"${round(summen,2)-3} money back")
                print("Enjoy your coffee")
                money+=3
            if summen == 3:
                print("Enjoy your coffee")
                money+=3
            if summen < 3:
                print(f"You need ${3-round(summen,2)}")
    else:
        on = False


#hvor mye reusrser 

#process coins

#chenck if transactions sucsessful

#make coffe

#reduce resurser 



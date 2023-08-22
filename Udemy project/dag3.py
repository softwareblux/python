# water_level = 50

# if water_level > 80:
#     print("drain water")

# else:
#     print("continue")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height < 120:
#     print("acsess denied, bitch, suck your mom")

# else:
#     print("Welcome aboard")

# number = int(input("Which number do you want to check? "))

# number1 = number%2

# if number1 == 1:
#     print(f"{number} is a odd number")

# else:
#     print(f"{number} is a even number")



# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("Welcome aboard")
#     age = int(input("what is your age? "))
#     if age < 12:
#         print("your price is $5")

#     elif age <= 18:
#         print("your price is $7")


#     else:
#         print("your price is $12")
        

# else:
#     print("acsess denied, bitch, suck your mom")


# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight/(height/100)**2, 2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")

# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you are normal weight.")

# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")

# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")

# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# year = int(input("Which year do you want to check? "))

# if year%4 == 0:
#     if year%100 == 1:
#         print("its a leap year")

#     elif year%400 == 0:
#         print("its a leap year")
    
#     else:
#         print("no leap year")
# else:
#     print("not a leap yeat")

  
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("Welcome aboard")
#     age = int(input("what is your age? "))
#     if age < 12:
#         bill = 5
#         print("child tickets are $5")

#     elif age <= 18:
#         bill = 7
#         print("youth tickets are $7")


#     else:
#         bill = 12
#         print("adult tickets are $12")
    
#     bilde = input("Do you want a photo taken? Yes or no? ")

#     if bilde == "yes":
#         bill += 3


#     print(f"Your final bill is ${bill}")


# else:
#     print("acsess denied, bitch, suck your mom")


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0 

# if size == "s":
#     bill += 15
#     if add_pepperoni == "y":
#         bill += 2
#     if extra_cheese == "y":
#         bill += 1
#     print(f"Your bill is ${bill}")

# elif size == "m":
#     bill += 20
#     if add_pepperoni == "y":
#         bill += 3
#     if extra_cheese == "y":
#         bill += 1
#     print(f"Your bill is ${bill}")

# elif size == "l":
#     bill += 25
#     if add_pepperoni == "y":
#         bill += 3
#     if extra_cheese == "y":
#         bill += 1
#     print(f"Your bill is ${bill}")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("Welcome aboard")
#     age = int(input("what is your age? "))
#     if age < 12:
#         bill = 5
#         print("child tickets are $5")

#     elif age <= 18:
#         bill = 7
#         print("youth tickets are $7")

#     elif age >= 45 and age <= 55:
#         print("midlife crisis tickets are $0")

#     else:
#         bill = 12
#         print("adult tickets are $12")
    
#     bilde = input("Do you want a photo taken? Yes or no? ")

#     if bilde == "yes":
#         bill += 3


#     print(f"Your final bill is ${bill}")


# else:
#     print("acsess denied, bitch, suck your mom")


# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# both = name1 + name2

# both_low = both.lower()

# t =  both.count("t")
# r =  both.count("r")
# u =  both.count("u")
# e =  both.count("e")

# l =  both.count("l")
# o =  both.count("o")
# v =  both.count("v")
# e =  both.count("e")

# true = t + r + u + e
# love = l + o + v + e

# love_score = int(str(true) + str(love))

# #int_score = int(love_score)

# if (love_score < 10) or (love_score > 90):
#    print(f"Your score is {love_score}, you go together like coke and mentos.")

# elif (love_score <= 50) and (love_score >= 40):
#    print(f"Your score is {love_score}, you are alright together.")

# else:
#    print(f"Your score is {love_score}.")

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# lr = input("you're at a cross road. where do you want to go? Type left or right ")
# lre = lr.lower()

# if lre == "left":
    
#     sw = input("swim or wait? ")
#     swe = sw.lower()
    
#     if swe == "wait":
        
#        byr =  input("which door? blue, yellow red ")
#        byre = byr.lower()
    
#     if byre == "blue":
#         print(" you got eaten by eddie hall. game over")

#     elif byre == "yellow":
#         print("you have won the game!!")

#     elif byre == "red":
#         print("enjoy  the flames bitch. GAME OVER.")

#     else:
#         print("Game over biatch")
    
#     #elif  == "blue":
    
    
    
# else:
#     print("Fall into a hole. Game over")







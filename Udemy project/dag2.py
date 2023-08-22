#print(len("helllo"))

#k = "hello kr" #subscript er det at du henter ut en verdi fra en string for eksempel. og bruker [] for og du begynner alltid med 0 for å få første verdi mellom rom er også en del når du begynner å telle

#print(k[4] + k[6]) 


#integer

#print(123 +345)

#print(100_000_000 + 100_000)

#float

#3.14159


#boolean

#True
#False

#num_char = len( input("hva er ditt navn?"))
#new_num_char = str(num_char)
#print("ditt navn har " + new_num_char + " bokstaver")

#print(type(num_char))


#a = float(123.08)

#print(type(a))

#print(70 + float("105.5"))


# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇


# BMI = ((int(weight))/(float(height)**2))

# BMIsomheltall = int(BMI)

# print(BMIsomheltall)


# print(8 // 3)

# score = 0 


# score += 1

# print(score)


# score = 0 
# height = 1.8
# iswinning = True
# #f-string
# print(f"your score is {score}, your height {height}, you are winning is {iswinning}")

age = input("What is your current age? ")

dager = (90 - int(age))*365
uker = (90 - int(age))*52
maaned = (90 - int(age))*12


print(f"You have {dager} days, {uker} weeks, and {maaned} months left to live ")


# pris = float(input("What was the total bill? $"))
# prosent = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
# folk = int(input("how many people to split the bill "))

# proc = float(prosent)/100 + 1

# pris_per_pers = round((pris/folk)*proc, 2)

# pris_per_pers = "{:.2f}".format(pris_per_pers)

# print(f"Each person should pay: ${pris_per_pers}")

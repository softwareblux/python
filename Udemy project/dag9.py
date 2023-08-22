# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# print(programming_dictionary["Bug"])

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91:
#         student_grades[student] = "outstanding"

#     elif score >= 81:
#         student_grades[student] = "Exceeds expectation"

#     elif score >= 71:
#         student_grades[student] = "Acceptable"

#     else:
#         student_grades[student] = "fail"



# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["Visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# print(travel_log)


import sys, os

loop = True
bids = {}

def find_highest_bidder(bidrec):
  highest_bid = 0
  winner = ""
  for bidder in bidrec:
    bid_amount = bidrec[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest_bid}")



while loop:

  print("Hello, welcome to the secret auction program.")
  navn = input("What is your name? ")
  
  bid = int(input("What is your bid? $"))
  
  bids[navn] = bid

  howmany = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  if howmany == "no":
    loop = False
    find_highest_bidder(bids)
  
  elif howmany == "yes":
    os.system('cls')

    
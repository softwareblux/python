# fruits = ["apple", "orange", "pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#     print(fruits)

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])


# total = 0

# for height in student_heights:
#   total += height
# #print(total)

# num = 0

# for student in student_heights:
#    num += 1
# #print(num)

# avrage = round(total/num)
# print(avrage)

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highscore = 0 

# for score in student_scores:
#   if score > highscore:
#     highscore = score
# print(f"The highest score in the class is: {highscore}")


# for number in range(1, 11, 3):
#     print(number)




# total = 0

# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number

# print(total)

# total2 = 0

# for number in range(2, 101, 2):
#     total2 += number

# print(total2)



# total = 0 

# for number in range (1, 101):

    
#     if number % 3 == 0 and number % 5 == 0:
    
#         number = "FizzBuzz"
    
#     elif number % 3 == 0:
    
#         #print("Fizz")
#         number = "Fizz"

#     elif number % 5 == 0:
    
#        number = "Buzz"

    
    
#     print(number)



import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# passord = ""

# for letter in range(0, nr_letters+1):
#     random_number_of_letters = random.choice(letters)

#     passord += random_number_of_letters

# for symbol in range(0, nr_symbols+1):
#     random_number_of_symbols = random.choice(symbols)

#     passord += random_number_of_symbols

# for number in range(0, nr_numbers+1):
#     random_number_of_numbers = random.choice(numbers)

#     passord += random_number_of_numbers



# print(passord)


passord_list = []

for letter in range(0, nr_letters):
    random_number_of_letters = random.choice(letters)

    passord_list.append(random_number_of_letters)

for symbol in range(0, nr_symbols):
    random_number_of_symbols = random.choice(symbols)

    passord_list.append(random_number_of_symbols)

for number in range(0, nr_numbers):
    random_number_of_numbers = random.choice(numbers)

    passord_list.append(random_number_of_numbers)



#print(passord_list)

random.shuffle(passord_list)

#print(passord_list)

passord = ""

for each in passord_list:
    passord += each

print(f"Your password is {passord}")

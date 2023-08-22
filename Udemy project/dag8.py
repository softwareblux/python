import math
from dag8_art import logo
# def greet(name):
#     print(f"Hello {name}")
#     print("The TOP")
#     print("G")

# greet(input("what is your name "))


# def hello(name, location):
#     print(f"hello {name}")
#     print(f"{location} is a nice city ")

# hello(name=input("what is your name? "), location=input("Where are you from? "))


#Write your code below this line 👇

# def paint_calc(height, width, cover):
#     print(math.ceil((height*width)/cover))






# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)




#Write your code below this line 👇
def prime_checker (number): 
    isprime = True
    for i in range(2, number):
        
        if number % i == 0:
            isprime = False
    if isprime % i == 1:
        print("its a prime")
    else:
        print("no prime")


    
    



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def caesar(all_text, shift_amount, dir):
#    if dir == "encode":
      
#         cipher_text = ""
#         for letter in all_text:
#             position = alphabet.index(letter)
#             new_position = position + shift_amount
#             cipher_text += alphabet[new_position]
#         print(f"The encoded text is {cipher_text}")

#    elif dir == "decode":

#         plain_text = ""
#         for letter in all_text:
#             position = alphabet.index(letter)
#             new_position = position - shift_amount
#             plain_text += alphabet[new_position]
#         print(f"The decoded text is {plain_text}")


# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(all_text=text, shift_amount=shift, dir=direction)

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")


# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
       end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
should_con = True
while should_con:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

    shift = shift%26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("type yes tou continue type no to stop.\n")
    if result == "no":
       should_con = False
    
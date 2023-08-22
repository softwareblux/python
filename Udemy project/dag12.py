# enemies = 1

# def increase_enemies():
#   global enemies
#   enemies += 1
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# gameLevel = 1 
# def ceate_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]

#     if gameLevel < 5:
#         new_enemie = enemies[0]

#     print(new_enemie)

# ceate_enemy()
import random



print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 to 100.")
eorh = input("Choose a difficulty. Type 'easy' or 'hard': ")
randomNumber = random.randint(0,100)

if eorh.lower == "easy":
    numbero = 10
    


else:
    numbero = 5
    

game = True

print(randomNumber)

while game:
    
    
    print(f"you have {numbero} attempts to guess the number")
    
    guess = int(input("make a guess: "))

    if guess == randomNumber:
        print("You WWWWOOOONNNNN")
        game = False
    
    elif numbero < 2:
        game = False
    
    elif guess > randomNumber:
        print("TOOO HIGH")

    else:
        print("Too LOW")
    numbero -= 1 
    

    




#  ############### Blackjack Project #####################

# #Difficulty Normal 😎: Use all Hints below to complete the project.
# #Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# #Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# #Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############### Our Blackjack House Rules #####################

# ## The deck is unlimited in size. 
# ## There are no jokers. 
# ## The Jack/Queen/King all count as 10.
# ## The the Ace can count as 11 or 1.
# ## Use the following list as the deck of cards:
# ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ## The cards in the list have equal probability of being drawn.
# ## Cards are not removed from the deck as they are drawn.
# ## The computer is the dealer.

# import random


# def deal():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#     card = random.choice(cards)
#     return card


# num1 = deal()
# num2 = deal()
# ncards = [num1, num2]
# sum_ncards = sum(ncards)

# print(f"Your cards: {ncards}, current score {sum_ncards}")


# comnum1 = deal()
# comnum2 = deal()

# computer_card1 = [comnum1]

# computer_sum = sum(computer_card1)

# print(f"Computer first card: {computer_sum}")

# computer_cards = [comnum1, comnum2]

# computer_cards_sum = sum(computer_cards)

# play = True

# new_sum = 0


# while play:
#     l = input("Type 'y' to play and press 'n' to pass: ")
#     if l == "y":
#         ncards.append(deal())
#         new_sum = sum(ncards)
#         print(f"Your cards: {ncards}, current score {new_sum}")
        

#         if new_sum > 21:
#             print("You lose")
#             play = False
        

#     else:
        
#         if sum_ncards > newcom and sum_ncards<=21:
#             print("you wins")

#             play = False

#         elif new_sum > newcom and new_sum <= 21:
#             ncards.append(deal())
#             new_sum = sum(ncards)

#             print("You win")
        
#             play = False
        
#         else:
#             print("You lose")
#             play = False

    
    
# while not play:     
#     if computer_cards_sum < 16:
#                 computer_card1.append(deal())
                
#                 newcom = sum(computer_card1)

#                 print(f"machine card sum: {newcom}")


# #computer sum må være ovenfor siden jeg må kunne legge til kort etter jeg har takket nei.

## The deck is unlimited in size.

## There are no jokers.

## The Jack/Queen/King all count as 10.

## The the Ace can count as 11 or 1.

## Use the following list as the deck of cards:

## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## The cards in the list have equal probability of being drawn.

## Cards are not removed from the deck as they are drawn.

## The computer is the dealer.

 

import random
import dag11art
import os

os.system('cls')
print(dag11art.logo)

def deal():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

 

    card = random.choice(cards)

    return card

 

# computer cards

computer_cards =[deal(),deal()]
computer_sum = sum(computer_cards)

# player cards

player_cards = [deal(),deal()]

player_sum = sum(player_cards)

print("Your cards: "+str(player_cards))
print("you sum is: " + str(player_sum))
print("House: "+str(computer_cards[0]))

new_sum = 0

p_play = True

c_play = True

while p_play:

    l = input("Type 'y' to play and press 'n' to pass: ")

    if l == "y":

        player_cards.append(deal())

        player_sum = sum(player_cards)

        print(f"Your cards: {player_cards}, current score {player_sum}")
    
    if l == 'n':
        p_play = False    

 

    if player_sum > 21:

        print("you lose")
        p_play = False

 

while c_play:

    if computer_sum < 16:

        computer_cards.append(deal())

        computer_sum = sum(computer_cards)

    if computer_sum > 16:

        c_play = False


print("Your cards:"+str(player_cards)+" " + str(player_sum))
print("House: "+str(computer_cards) +" " + str(computer_sum))


if player_sum > computer_sum:

    if player_sum>21:
        print('you LOSE')
    else: 
        print("you win")


elif computer_sum > player_sum:
    if computer_sum> 21 and player_sum < 21:
        print("you WIN")
    
    else:
        print('You lost')

elif computer_sum == player_sum:
    if player_sum > 21:
        print("you lose")
    else:
        print("DRAW")


    
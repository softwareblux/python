import random
import dag4_module


# random_int = random.randint(1, 10)

# print(random_int)

# #print(dag4_module.pi)


# random_float1 = random.random() * 5

# print(random_float1)

# love_score = random.randint(1, 100)

# print(f"your love score is {love_score}%")



# head = 0
# tails = 1 

# coin = random.randint(0, 1)

# if coin == 0:
#     print("Head")

# else:
#     print("Tails")




# USA = ["delaware", "pennsylvania"]

# USA.append("land")

# USA.extend(["mucho", "suii"])

# print(USA)

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

#  nam = len(names)- 1

#  who = random.randint(0, nam)

# who = random.choice(names)


# print(f"{who} må betale")





# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# # print(map[0][1])


# x = int(position[0])
# y = int(position[1])

# # rad = map[y - 1]

# # rad[x - 1] = " X"

# map[y - 1][x-1] = " X"

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")




# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# ssp = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# rock > scissors
# scissors > paper
# paper > rock


# if ssp == 0: 
#     print(rock)

# elif ssp == 1:
#     print(paper)

# else:
#     print(scissors)


# ssp_list = [rock, paper, scissors]

# print("computer chose:")



# ssp_list_random = random.randint(0, 2)

# if ssp_list_random == 0: 
#     print(rock)

# if ssp_list_random == 1:
#     print(paper)

# if ssp_list_random == 2:
#     print(scissors)

# if ssp == 0 and ssp_list_random == 2:
#     print("you win!!")

# elif ssp > ssp_list_random:
#     print("you win!!")

# elif ssp == ssp_list_random:
#     print("draw!!")

# else:
#     print("you lose!!")




hvem = ["Kine", "Tuva", "Sandrine", "Beatriz", "PH", "Charli", "Kylie", "Amalie", "Sofie", "Ida Marie", "Kendall", "Jena", "Helen", "Maria", "Sarah", "Savanna", "Andrea", "Celine", "Andrine", "Sofie Hopland", "Aud Malin", "Martine"]

nuke = random.choice(hvem)

print("du skal runke til " + nuke)



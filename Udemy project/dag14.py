from dag14data import data
import random

game = True

a= random.choice(data)
b= random.choice(data)
if a == b:
    b= random.choice(data)



name1 = a['name']
description1 = a['description']
country1 = a['country']

print(f"{name1}, a {description1}, from {country1}")

name = b['name']
description = b['description']
country = b['country']

print(f"{name}, a {description}, from {country}")
# print(name1)
# print(follower_count1)
# print(description1)
# print(country1)
# while game:    
#     random_entity = random.choice(data)

#     name = random_entity['name']
#     follower_count = random_entity['follower_count']
#     description = random_entity['description']
#     country = random_entity['country']


#     print(name)
#     print(follower_count)
#     print(description)
#     print(country)
#     aobw = input("A or B?")
#     aob = aobw.lower
#     random_entity = random_entity1
#     if aob == "a":
#         if follower_count1 > follower_count:
#             random_entity = random_entity1
#         else:
#             game = False
    
#     elif aob == "b":
#         if follower_count1 < follower_count:
#             random_entity = random_entity1
#         else:
#             game = False
    






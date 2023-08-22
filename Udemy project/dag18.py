# from turtle import *
# import random

# # colorurs = ["blue", "red", "green", "purple"]

# tortuga = Turtle()

# # def draw_shape(num_sides):
# #     angle = 360/num_sides
# #     for i in range(num_sides):

# #         tortuga.right(angle)
# #         tortuga.forward(100)


# # for shape in range(3,11):
# #     tortuga.color(random.choice(colorurs))
# #     draw_shape(shape)

# tortuga.shape("turtle")
# angle = 90
# tortuga = Turtle()
# # colormode(255)
# def randomcolor():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# # colorurs = ["blue", "red", "green", "purple"]
# # random_directions = [0, 90, 180, 270]
# tortuga.pensize(10)
# tortuga.speed(0)

# for i in range(200):

#     tortuga.dot(20, randomcolor())
   
    
# # for i in range(360):
# #     tortuga.setheading(2*i )
# #     tortuga.circle(100, None, None)
# #     tortuga.color(randomcolor())
    

# tortuga.position()
# tortuga.shape("turtle")













# screen = Screen()
# screen.exitonclick()

from turtle import *
import random

screen = Screen()


tortuga = Turtle()
tortuga.hideturtle()
tortuga.penup()
# tortuga.pensize(10)
tortuga.speed(0)
colormode(255)


tortuga.setheading(225)
tortuga.forward(300)
tortuga.setheading(0)
tortuga.clear()

def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
for i in range(10):
    for i in range(10):
        tortuga.dot(20,randomcolor())
        tortuga.forward(50)
        
    for i in range(1):
        tortuga.setheading(90)
        tortuga.forward(50)
        tortuga.setheading(180)
        tortuga.forward(500)
        tortuga.setheading(0)
        



screen.exitonclick()
tortuga.position()
tortuga.shape("turtle")

from turtle import Turtle, Screen
import random

isracone= False
screen = Screen()
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
yt = [-100,-75,-50,-25,0,25]
screen.setup(500,400)
bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? enter the color: ")
totles = []

for i in range (0,6):
    tortuga = Turtle(shape="turtle")
    tortuga.color(colors[i])
    tortuga.penup()
    tortuga.goto(x=-235, y= yt[i])
    totles.append(tortuga)

if bet:
    isracone = True

while isracone:
    for tortuga in totles:
        if tortuga.xcor()>230:
            isracone = False
            wincol = tortuga.pencolor()
            if wincol == bet:
                
                print(f"DU VANT! FARGEN VAR {wincol}")
            else:
                print(f"DU tapte! FARGEN VAR {wincol}")
        
        

        fart = random.randint(0,10)
        tortuga.forward(fart)


screen.exitonclick()
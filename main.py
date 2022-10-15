from turtle import Turtle, Screen
import random
Screen().screensize(1000, 1000)
Screen().title("Turtles race")
colors = ['red', 'blue', 'yellow', 'green', 'black', 'purple']
user = Screen().textinput("Bet", f"choose your bet from {colors}")
y = -150
turtles = []

for x in range(6):
    t = Turtle("turtle")
    t.penup()
    t.color(colors[x])
    t.shapesize(stretch_wid=2)
    t.setposition(-250, y)
    y += 50
    turtles.append(t)
game = True
while game:
    for turtle in turtles:
        turtle.fd(random.randint(0, 10))
        if turtle.xcor() == 250:
            game = False
            xcor = 0
            for turtle in turtles:
                if turtle.xcor() > xcor:
                    xcor = turtle.xcor()
            for turtle in turtles:
                if turtle.xcor() == xcor:
                    winner = turtle.pencolor()

if winner.lower == user.lower:
    print("congratulations you win")
else:
    print(f"{winner} win you lose")
print("good bye")









Screen().exitonclick()
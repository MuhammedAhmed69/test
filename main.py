from turtle import Turtle, Screen
Screen().screensize(1000, 1000)
Screen().title("Turtles race")
colors = ['red', 'blue', 'yellow', 'green', 'black', 'purple']
Screen().textinput("Bet", f"choose your bet from {colors}")
y = -150
for x in range(6):
    t = Turtle("turtle")
    t.penup()
    t.color(colors[x])
    t.shapesize(stretch_wid=2)
    t.setposition(-250, y)
    y += 50








Screen().exitonclick()
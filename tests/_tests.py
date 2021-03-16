from turtle import Screen, Turtle
import pip

screen = Screen()
turtle = Turtle()

turtle.color('black', 'red')
turtle.begin_fill()
for n in range(1, 10):
    for i in range(round(360 / (n * 5))):
        turtle.forward(10)
        turtle.left(5 * n)
turtle.end_fill()
screen.mainloop()

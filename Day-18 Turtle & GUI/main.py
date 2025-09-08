from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red")

for _ in range(0, 4):
    tim.forward(100)
    tim.right(90)

screen.exitonclick()

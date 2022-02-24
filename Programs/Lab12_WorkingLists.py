# Name: James R. Laurita
# Date: 2.24.2022
# Lab10: Working with lists
# Description: Use lists to change color of turtle object then alter list.

def main():

    import turtle
    import math
    import random

    turtle.setup(800, 800)
    win = turtle.Screen()
    win.bgcolor("Forest Green")

    speedy = turtle.Turtle()
    speedy.hideturtle()
    speedy.pensize(2)
    speedy.speed(0)

    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]

    userColor = input("What color would you like added? ")
    colors[1] = userColor
    colors.remove("cyan")
    colors.append("chartreuse")
    colors[2] = "firebrick"

    print(colors)

    index = 0

    for x in range (500):
        speedy.color(colors[index])
        speedy.forward(x)
        speedy.right(98)
        index = (index + 1) % len(colors)

    turtle.mainloop()

if __name__ == "__main__":
    main()
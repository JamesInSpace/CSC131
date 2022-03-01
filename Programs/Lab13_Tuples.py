# Name: James R. Laurita
# Date: 3.01.2022
# Lab10: Working with tuples
# Description: Creating color wheel using tuples.

def main():

    import turtle
    import math
    import random

    turtle.setup(800, 800)

    speedy = turtle.Turtle()
    speedy.hideturtle()
    speedy.speed(0)
    speedy.pensize(2)
    speedy.penup()
    speedy.goto(-150,0)
    speedy.pendown()

    colorList = []
    numberOfColors = 500
    numberOfSteps = numberOfColors / 6
    colorIncrement = 1 / numberOfSteps

    intensityOfRed = 1.0
    intensityOfGreen = 0.0
    intensityOfBlue = 0.0

    while intensityOfGreen < 1.0 - colorIncrement:
        colorTup = (intensityOfRed, intensityOfGreen, intensityOfBlue)
        colorList.append(colorTup)
        intensityOfGreen += colorIncrement

    while intensityOfRed > 0.0 + colorIncrement:
        colorTup = (intensityOfRed, intensityOfGreen, intensityOfBlue)
        colorList.append(colorTup)
        intensityOfRed -= colorIncrement

    while intensityOfBlue < 1.0 - colorIncrement:
        colorTup = (intensityOfRed, intensityOfGreen, intensityOfBlue)
        colorList.append(colorTup)
        intensityOfBlue += colorIncrement

    while intensityOfGreen > 0.0 + colorIncrement:
        colorTup = (intensityOfRed, intensityOfGreen, intensityOfBlue)
        colorList.append(colorTup)
        intensityOfGreen -= colorIncrement

    while intensityOfRed < 1.0 - colorIncrement:
        colorTup = (intensityOfRed, intensityOfGreen, intensityOfBlue)
        colorList.append(colorTup)
        intensityOfRed += colorIncrement

    while intensityOfBlue > 0.0 + colorIncrement:
        colorTup = (intensityOfRed, intensityOfGreen, intensityOfBlue)
        colorList.append(colorTup)
        intensityOfBlue -= colorIncrement


    for x in colorList:
        speedy.color(x)
        speedy.forward(300)
        speedy.right(180+180/len(colorList))


    turtle.mainloop()

if __name__ == "__main__":
    main()
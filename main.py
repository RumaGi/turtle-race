import random
import turtle

race_is_on = False

screen = turtle.Screen()
screen.setup(width=800, height=700)

colors = ["red", "blue", "coral", "gold", "navy", "black", "sienna", "teal", "dark olive green"]
y_coordinate = [200,
                150, 100, 50, 0, -50, -100, -150, -200]
turtles =[]

for i in range(0, 9):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.shapesize(2, 2, 5)
    new_turtle.color(colors[i])
    new_turtle.goto(-380, y_coordinate[i])

    turtles.append(new_turtle)

color_entered = screen.textinput(title="Make your bet",
                                 prompt=f"Enter the color of the turtle you want to bet on --> ({', '.join(colors)}) ").lower()


if color_entered:
    race_is_on = True

while race_is_on:

    for turtle in turtles:
        if turtle.xcor() >= 340:
            race_is_on = False
            print(f"\n{turtle.pencolor().capitalize()} colored turtle won the race")
            print(f"\nThe color you entered was {color_entered.capitalize()}")

            if turtle.pencolor().lower() != color_entered.lower():

                print("\nYou lost the bet.")
                break
            else:
                print("\nYou won the best!!!")
                break

        turtle.speed("fastest")
        turtle.forward(random.randint(0, 30))

screen.exitonclick()


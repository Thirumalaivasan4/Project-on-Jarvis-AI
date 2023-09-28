from turtle import *
import turtle
import time
import pyautogui
def heart():
    color("red")
    begin_fill()
    pensize(3)
    left(50)
    forward (133)
    circle(50,200)
    right (140)
    circle (50,200)
    forward(133)
    end_fill()
    time.sleep(2.5)
def IronMan():
    # Create a turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle object
    iron_man = turtle.Turtle()
    iron_man.speed(1)

    # Define colors
    red = (1, 0, 0)
    gold = (1, 0.843, 0)

    # Define a function to draw a rectangle
    def draw_rectangle(x, y, width, height, color):
        iron_man.penup()
        iron_man.goto(x, y)
        iron_man.pendown()
        iron_man.color(color)
        iron_man.begin_fill()
        for _ in range(2):
            iron_man.forward(width)
            iron_man.left(90)
            iron_man.forward(height)
            iron_man.left(90)
        iron_man.end_fill()

    # Draw Iron Man's head
    draw_rectangle(-50, 100, 100, 100, gold)

    # Draw Iron Man's body
    draw_rectangle(-50, 0, 100, 100, red)

    # Close the window when clicked
    screen.exitonclick()
    
def welecomemsg():

    # Create a turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle object
    welcome_turtle = turtle.Turtle()
    welcome_turtle.speed(1)  # Set the drawing speed (1 is slow)

    # Define a function to write a message
    def write_welcome_message():
        welcome_turtle.penup()  # Lift the pen to move without drawing
        welcome_turtle.goto(0, 0)  # Move the turtle to the desired position
        welcome_turtle.pendown()  # Put the pen down to start drawing
        welcome_turtle.color("blue")  # Set the text color
        welcome_turtle.write("Welcome to Python Turtle!", align="center", font=("Arial", 24, "normal"))
        welcome_turtle.penup()  # Lift the pen again

    # Call the function to write the welcome message
    write_welcome_message()

    # Close the window when clicked
    screen.exitonclick()
    pyautogui.click(1418,151)
if __name__ == "__main__":
    #welecomemsg()

    #IronMan()
    heart()
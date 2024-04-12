"""TODO: Describe your scene program."""
__author__ = "Your PID"
	 
from turtle import Turtle, colormode, done 


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, height: float, color: str) -> None:
    """Function to draw rectangles for houses and windows."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor(color)
    a_turtle.begin_fill()
    for _ in range(2):
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.left(90)
    a_turtle.end_fill()


def draw_triangle(a_turtle: Turtle, x: float, y: float, width: float, color: str) -> None:
    """Function to draw the triangle roof"""
    height = width * 0.5 * 3 ** 0.5  # Calculate the height of an equilateral triangle
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor(color)
    a_turtle.begin_fill()
    a_turtle.setheading(60)  # Starting angle
    for _ in range(3):
        a_turtle.forward(width)
        a_turtle.right(120)
    a_turtle.end_fill()


def draw_windows(a_turtle: Turtle, x: float, y: float, width: float, height: float, count: int) -> None:
    """Recursive function to draw windows on the house."""
    if count == 0:
        return
    else:
        draw_rectangle(a_turtle, x, y, width, height, "lightblue")  # Draw one window
        # Recursively draw the rest of the windows spaced by the width of a window + 10 pixels
        draw_windows(a_turtle, x + width + 10, y, width, height, count - 1)


def draw_sun(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Function to draw the sun with a filled yellow color"""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor("yellow")
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


def main() -> None:
    """The entrypoint of my scene to construct the house and the sun."""
    # Set up the turtle object
    house_turtle: Turtle = Turtle()
    house_turtle.speed(0)  # Fastest drawing speed

    # Draw the sun
    draw_sun(house_turtle, 200, 150, 50)

    # Draw the house body
    draw_rectangle(house_turtle, -150, -150, 200, 150, "grey")

    # Draw the roof of the house
    draw_triangle(house_turtle, -150, 0, 200, "red")

    # Draw the door
    draw_rectangle(house_turtle, -100, -150, 40, 60, "brown")

    # Draw the windows using recursion
    draw_windows(house_turtle, -140, -60, 30, 30, 5)  # Draw 5 windows

    # Finish drawing
    done()


if __name__ == "__main__":
    main()

	 
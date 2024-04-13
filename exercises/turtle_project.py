"""Houses with Windows."""
__author__ = "730679888"

from turtle import Turtle, colormode, done


def draw_vertical_rectangle(a_turtle: Turtle, x: float, y: float, width: float, height: float, color: str) -> None:
    """Draw a vertical rectangle with the bottom-left corner at (x, y)."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0) 
    a_turtle.pendown()
    a_turtle.fillcolor(color)
    a_turtle.begin_fill()
    for i in range(2): 
        a_turtle.forward(width)
        a_turtle.left(90)
        a_turtle.forward(height)
        a_turtle.left(90)
    a_turtle.end_fill()


def draw_triangle(a_turtle: Turtle, x: float, y: float, width: float, color: str) -> None:
    """Function to draw the triangle roof."""
    height = width * 0.5 * (3 ** 0.5)  # Calculate the height of an equilateral triangle
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
        draw_vertical_rectangle(a_turtle, x, y, width, height, "lightblue")
        draw_windows(a_turtle, x + (width + 10), y, width, height, count - 1)


def draw_sun(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Function to draw the sun with a filled yellow color."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.fillcolor("yellow")
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


def main() -> None:
    """The entrypoint of my scene to construct the house and the sun."""
    house_turtle: Turtle = Turtle()
    house_turtle.speed(0) 
    draw_sun(house_turtle, 200, 150, 50)
    draw_vertical_rectangle(house_turtle, -150, -150, 200, 150, "grey")
    draw_triangle(house_turtle, -150, 0, 200, "red")
    draw_vertical_rectangle(house_turtle, -100, -150, 40, 60, "brown")
    windows_start_y = -90 
    windows_spacing = 30 + 10  
    draw_windows(house_turtle, -140, windows_start_y, 30, 30, 5)  

    done()


if __name__ == "__main__":
    main()
"""EX02 - One Shot Battleship."""
__author__ = "730679888"
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

grid_size = 4
secret_row = 3
secret_column = 2

guessed_row = 0
guessed_column = 0

while guessed_row < 1 or guessed_row > grid_size:
    row_input = input("Guess a row: ")
    if row_input == '1' or row_input == '2' or row_input == '3' or row_input == '4':
        guessed_row = int(row_input)
    else:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")

while guessed_column < 1 or guessed_column > grid_size:
    column_input = input("Guess a column: ")
    if column_input == '1' or column_input == '2' or column_input == '3' or column_input == '4':
        guessed_column = int(column_input)
    else:
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")

row_color = 1
while row_color <= grid_size:
    row_str = ""
    column_color = 1
    while column_color <= grid_size:
        if row_color == guessed_row and column_color == guessed_column:
            if row_color == secret_row and column_color == secret_column:
                row_str += RED_BOX
            else:
                row_str += WHITE_BOX
        else:
            row_str += BLUE_BOX
        column_color += 1
    print(row_str)
    row_color += 1

if guessed_row == secret_row and guessed_column == secret_column:
    print("Hit!")
else:
    print("Miss!")
    if guessed_row == secret_row:
        print("Close! Correct row, wrong column.")
    elif guessed_column == secret_column:
        print("Close! Correct column, wrong row.")
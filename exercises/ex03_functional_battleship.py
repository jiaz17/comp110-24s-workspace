"""Ex03 - Functional Battleship."""

__author__ = "730679888"
import random

BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"


def input_guess(grid_size: int, specification: str) -> int:
    """Guessed row and column."""
    assert specification == "row" or specification == "column", "Specification must be 'row' or 'column'."
    while True:
        guess_input = input(f"Guess a {specification}: ")
        valid_guess = False
        guess_number = 1
        while guess_number <= grid_size:
            if guess_input == str(guess_number):
                valid_guess = True
                break
            guess_number += 1

        if valid_guess:
            return int(guess_input)
        
        print(f"The grid is only {grid_size} by {grid_size}. Try again: ")

        
def print_grid(grid_size: int, row_guess: int, column_guess: int, whether_correct: bool) -> None:
    """Grid size determination."""
    row = 1
    while row <= grid_size:
        row_str = ""
        column = 1
        while column <= grid_size:
            if row == row_guess and column == column_guess:
                row_str += RED_BOX if whether_correct else WHITE_BOX
            else:
                row_str += BLUE_BOX
            column += 1
        print(row_str)
        row += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Input correct guess."""
    return row_guess == secret_row and column_guess == secret_column


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Start the main game loop."""
    turns = 5
    turns_used = 0
    whether_correct = False

    while turns_used < turns and not whether_correct:
        print(f"=== Turn {turns_used + 1}/{turns} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        whether_correct = correct_guess(secret_row, secret_column, row_guess, column_guess)

        print_grid(grid_size, row_guess, column_guess, whether_correct)

        if whether_correct:
            print(f"Hit! You won in {turns_used + 1}/{turns} turns!")
        else:
            print("Miss!")
            turns_used += 1

    if not whether_correct:
        print(f"X/{turns} - Better luck next time!")


if __name__ == "__main__":
    grid_size = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
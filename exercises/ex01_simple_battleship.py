"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730679888"
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

boat_location = int(input("Pick a secret boat location between 1 and 4: "))
if boat_location < 1:
    print("Error! 0 too low!")
    exit()
elif boat_location > 4:
    print("Error! 5 too high!")
    exit()

guess = int(input("Guess a number between 1 and 4: "))
if guess < 1:
    print("Error! 0 too low!")
    exit()
elif guess > 4:
    print("Error! 5 too high!")
    exit()
    
if guess == boat_location:
    print("Correct! You hit the ship.")
    result = RED_BOX
else:
    print("Incorrect! You missed the ship.")
    result = WHITE_BOX

full_emoji_string = ""
if guess == 1:
    if boat_location == 1:
        full_emoji_string = RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
    else:
        full_emoji_string = WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
elif guess == 2:
    if boat_location == 2:
        full_emoji_string = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX
    else:
        full_emoji_string = BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX
elif guess == 3:
    if boat_location == 3:
        full_emoji_string = BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX
    else:
        full_emoji_string = BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX
elif guess == 4:
    if boat_location == 4:
        full_emoji_string = BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX
    else:
        full_emoji_string = BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX
print(full_emoji_string)
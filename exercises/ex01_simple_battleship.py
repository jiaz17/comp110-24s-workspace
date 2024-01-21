"""EX01 - Simple Battleship - A cute step toward Battleship"""

__author__ = "730679888"
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U0001F7EB"

boat_location = int(input("Pick a secret boat location between 1 and 4: "))
if boat_location < 1:
    print("Error! 0 too low!")
elif boat_location > 4:
    print("Error! 5 too high!")
full_emoji_string = BLUE_BOX * 4
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

full_emoji_string = full_emoji_string[:guess-1] + result + full_emoji_string[guess:]
print(full_emoji_string)

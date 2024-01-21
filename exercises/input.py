"""Practice with variables and input function"""
#input always returns as string
first_name: str = input("What is your name?")
fav_number_str: input("What is your favorite number?")
fav_number: int = (fav_number_str)
higher_number: int = fav_number + 1
print("Hello" + first_name + "!")
print("My favorite number is" + str(higher_number))

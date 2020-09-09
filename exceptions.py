#Get player data
name = input("Please enter your name: ").capitalize()
age = input("Please enter your age: ")
try:
    print("You were born in {}.".format(2020 - int(age)))
except TypeError:
    print("Unable to perform mathematical operation of string and number")
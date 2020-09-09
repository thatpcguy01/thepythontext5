#Escape from DC

#Weapon Classes
class Weapon:
    #Define str function to return the name
    def __str__(self):
        return self.name
class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "An ordinary rock used for bludgeoning."
        self.damage = 5

class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "A small and sharp blade. Can be used for skinning as well as defense."
        self.damage = 10

class Bow(Weapon):
    def __init__(self):
        self.name = "Bow"
        self.description = "A wooden stick with an attached nylon string for long-range shooting"
        self.damage = 12
        self.arrow = 0

class Handgun(Weapon):
    def __init__(self):
        self.name = "Handgun"
        self.description = "A wooden stick with an attached nylon string for long-range shooting"
        self.bullets = 0
        self.damage = 30


def get_player_command():
    return input("Input direction: ")

def play():
    #Prints name of the game to player
    print("Escape from DC")
    #Print action commands
    print('''
    Valid directions: 
    n or N = North
    s or S = South
    e or E = East
    w or W = West
    i or I = Inventory
    ''')
    #Initialize & set variables
    action_input = get_player_command()
    inventory = [Rock(), "Bullets", "Stale Bread", "Medpack"]
    items = ["apple", "shoygun shells", "shotgun"]
    if action_input in ["n", "N"]:
        print("Go North!")
    elif action_input in ["s", "S"]:
        print("Go South!")
    elif action_input in ["e", "E"]:
        print("Go East!")
    elif action_input in ["w", "W"]:
        print("Go West!")
    elif action_input in ["i", "I"]:
        print("Inventory ")
        print (inventory)
    elif action_input in ["l", "L"]:
        print("Searching area...\n Found items: ")
        print(items[2])
    else:
        print("Invalid direction. Please type a valid direction.")
play()
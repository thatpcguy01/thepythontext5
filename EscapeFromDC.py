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
        self.damage = 20


def get_player_command():
    return input("Input direction: ")

def most_powerful_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass
    return best_weapon


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
    m or M = Show the most powerful weapon you've acquired
    ''')


    #Initialize & set variables
    action_input = get_player_command()
    inventory = [Rock(), "Bullets", "Stale Bread", "Medpack", Handgun()]

    items = ["apple", "shotgun shells", "shotgun"]
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
    elif action_input in ["m", "M"]:
        print("The most powerful weapon you have is the " + str(most_powerful_weapon(inventory)))
    else:
        print("Invalid input. Please type a valid direction.")
play()
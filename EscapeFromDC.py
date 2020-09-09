#Escape from DC

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
    inventory = ["Handgun", "Bullets", "Stale Bread", "Medpack"]
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
    else:
        print("Invalid direction. Please type a valid direction.")
play()
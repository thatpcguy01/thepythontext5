#Escape from DC


from player import Player
import items

def play():
    print("Escape from DC")
    #Player commands
    print('''
    Valid directions: 
    n or N = North
    s or S = South
    e or E = East
    w or W = West
    i or I = Inventory
    m or M = Show the most powerful weapon you've acquired
    ''')

    player = Player()

    while True:
        action_input = get_player_command()
        #Handle player commands
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
            #print (inventory)
            player.print_inventory()
        elif action_input in ["l", "L"]:
            player.print_inventory()
        elif action_input in ["m", "M"]:
            player.most_powerful_weapon(inventory)
            #print("The most powerful weapon you have is the " + str(most_powerful_weapon(inventory)))
        else:
            print("Invalid input. Please type a valid direction.")

def get_player_command():
    return input("Input direction: ")
play()
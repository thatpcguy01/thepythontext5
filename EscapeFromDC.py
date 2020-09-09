#Escape from DC

def get_player_command():
    return input("Input direction: ")

def play():
    print("Escape from DC")
    print('Valid directions: n,s,e,w')
    action_input = get_player_command()
    if action_input == 'n':
        print("Go North!")
    elif action_input == 's':
        print("Go South!")
    elif action_input == 'e':
        print("Go East!")
    elif action_input == 'w':
        print("Go West!")
    else:
        print("Invalid direction. Please type a valid direction.")
play()
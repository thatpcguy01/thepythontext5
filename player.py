import items

class Player:
    def __init__(self):
        self.inventory = [
            items.Handgun(),
            items.Knife(),
            'Cash(5)',
            'medpack']

    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print("*" + str(item))
            best_weapon = self.most_powerful_weapon()
            print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        print(best_weapon)
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
        self.arrows = 0
        self.damage = 20

class Handgun(Weapon):
    def __init__(self):
        self.name = "Handgun"
        self.description = "A wooden stick with an attached nylon string for long-range shooting"
        self.bullets = 0
        self.damage = 20
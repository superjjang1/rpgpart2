from character import Character

class Zombie(Character): #unkillable unit
    def __init__(self):
        super().__init__("Zombie", 0, 0) #no power, no health

    def alive(self):
        return 999999 #always alive
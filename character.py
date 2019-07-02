class Character(): # character class that holds all the information for the actual characters in game
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy): #attack command for both hero and goblin
        enemy.health -= self.power
        print("The %s does %d damage to the %s." % (self.name, self.power, enemy.name)) #what happens to the victim
            
    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power)) #printing the status of both

    def alive(self): #determines if character is alive or dead.
        return self.health > 0

class Zombie(Character): #unkillable unit
    def __init__(self):
        super().__init__("Zombie", 0, 0) #no power, no health

    def alive(self):
        return 999999 #always alive
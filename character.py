from random import randint
# character code, include damage modifiers,
# new character medic
# new character shadow
#z zombie never dies.
#two characters with individual characteristics, and implement them
# give each enemy a bounty



class Character(): # character class that holds all the information for the actual characters in game
    def __init__(self, name, job, health, power):
        self.name = name
        self.job = job #job title
        self.health = health
        self.power = power
        self.wealth = 20
        self.evasion = 0
        self.armor = 0
        self.bounty = 1
        self.inventory = []

        #job system and bounty part 6
        if self.job.lower() == 'hero':
            self.bounty = 10
        if self.job.lower() == 'medic':
            self.bounty = 9
        if self.job.lower() == 'shadow':
            self.bounty = 20
        if self.job.lower() == 'wizard':
            self.bounty = 30
        if self.job.lower() == 'zombie':
            self.bounty = 99999999
        if self.job.lower() == 'goblin':
            self.bounty = 2
        if self.job.lower() =='rhino':
            self.bounty = 20
        if self.job.lower() =='jackie':
            self.bounty = 100

    def attack(self, enemy): #attack command for both hero and other class
        damg = self.power #new variable to calculate damage
        if self.job.lower() == "hero": #only modifies for hero
            roll = randint(1,5) #modifier for damage to have a chance to do double damage
            if roll == 1:
                damg = self.power*2 #doubles the damage
                print("%s threw a critical hit!" % self.name)
        damg = int(damg * enemy.is_hit_factor()) 
        enemy.health -= damg #what happens to the health of the second character after attack
        print("The %s does %d damage to the %s." % (self.name, self.power, enemy.name)) #printed statement
        if enemy.job.lower() =="medic":
            roll = randint(1,5) #20% chance
            if roll == 1: #same as above for the chance to do something
                enemy.health += 2 #gain health on medic only
                print("%s has healed %d health!" % (enemy.name, 2)) #calls parameters

    def is_hit_factor(self): #unique modifiers
        hit = 1
        roll = 10
        if self.job.lower() == 'shadow': #10% chance to get hit
            roll = randint(1,10)
            if roll > 1:
                hit = 0 #didn't get hit
                print("%s dodged boyy!" % self.name)
        if self.job.lower() == 'rhino': #I'm the rhino bitchhhhh
            hit = 0.5 #takes half damage, rounded up.
        if self.job.lower() == 'jackie':
            roll = randint(1,2)
            if roll == 1: #get hit twice
                hit = 2
                print("%s forgot to switch to a stunt double and gets hit twice." %self.name)
            else:
                hit = 0
                print("%s is so fast, he dodged your attack." %self.name) #jackie is quick
        if self.job.lower() =='wizard':
            roll = randint (1,2)
            if roll == 1: #crazy damage
                hit = self.power*2 #doubles the damage or something crazy
                print("%s, you're a wizard's wizard!" % self.name)
        if self.evasion > 8:
            new_roll = randint(1,2)
            if new_roll ==1:
                hit = 0
        elif self.evasion > 4:
            new_roll = randint(1,100)
            if new_roll <= 15:
                hit = 0
        elif self.evasion > 2:
            new_roll = randint(1, 10)
            if new_roll == 1:
                hit = 0
            
        return hit



            
    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power)) #printing the status of both

    def alive(self): #determines if character is alive or dead.
        alive = self.health > 0
        if self.job.lower() == 'zombie': #zombie never dies lulululululul
            alive = True
        return alive

class Zombie(Character): #unkillable unit part 4
    def __init__(self):
        super().__init__("Zombie", 0, 0) #no power, no health

    def alive(self):
        return 999999 #always alive
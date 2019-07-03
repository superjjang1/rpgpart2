from character import *
from random import randint, choice

"""
In this simple RPG game, the hero fights somebody. He has the options to:
1. fight an enemy
2. do nothing - in which case the enemy will attack him anyway
3. flee
"""
"""
Character classes:
hero, medic, shadow, wizard, zombie, goblin, rhino, jackie

"""

def create_hero(): #dictionary list to call to input your class
    jobs_dict = {
        "1":"Hero",
        "2":"Medic",
        "3":"Shadow",
        "4":"Wizard",
        "5":"Rhino",
        "6":"Jackie"
    }
    print("Create your character!")
    name = input("What is your name small son?")
    job_select = input("What is your %s's class?\n1. Hero \n2. Medic\n3. Shadow\n4. Wizard\n5. Rhino\n6. Jackie\n:" % name)
    health = randint(100,150) #starting stats
    power = (randint(5,10)) #starting stats
    char = Character(name, jobs_dict[job_select], health, power)
    print("Your character has been created! %s the %s, your stats are %d health and %d power"% (name, char.job, char.health, char.power))
    return char

    

def main(char1):
    in_game = True
    while in_game: #kind of the base area the character is thrown into

        char_list = ['Hero', 'Medic', 'Shadow', 'Wizard', 'Rhino', 'Jackie', 'Zombie', 'Goblin']
        #list of the characters on the map, you can choose 6 of those, they don't include zombie or goblin
        action = input("Where you going?\n1. Travel\n2. Shop\n3. inventory(can't use items)\n4. Quit\n: ")
        #menu list of what you can do
        if action == "1": #starts the battle
            name = choice(char_list)
            char2 = Character(name, name, randint(20,60), randint(4,7)) 
            #char 2 name of char2, job, health, and power)
            print("%s has encountered %s!" % (char1.name, char2.name))
            battle(char1, char2)
        elif action == "2": #enter item shop
            Store(char1)
        elif action == "3": #use item that you chose
            use_item(char1)
        else: #quits out of game
            in_game = False
    
def battle(char1, char2): #fight between you and enemy
    fighting = True
    while char2.alive() and char1.alive() and fighting:
        char1.print_status()
        char2.print_status()
        print()
        print("What does %s want to do?" % char1.name)
        print("1. fight %s" % char2.name)
        print("2. Use item")
        print("3. Do nothing")
        print("4. Flee")
        # ^ is the menu in fight
        print(": ", end = "")
        user_input = input() #where you enter your input
        if user_input == "1": # you will attack the other character
            char1.attack(char2)
            if not char2.alive(): #when character dies gain moneys
                char1.wealth += char2.bounty
                print("%s is dead. %s gains %d gil, you now have %d gil" % (char2.name, char1.name, char2.bounty, char1.wealth))
        elif user_input == "2": # use item
            use_item(char1)
        elif user_input == "3": #do nothing
            pass
        elif user_input == "4": #running away, but you will retain damage
            print("smellyal8r loser.")
            fighting = False
        else:
            print("Invalid input %r. %s loses his turn" % (user_input, char1.name))

        if char2.alive(): #loop for when enemy can attack you
            char2.attack(char1) #how the second character attacks character 1
            if not char1.alive(): #so if you die your money goes to the enemy and you lose
                char2.wealth += char1.bounty
                print("%s is dead. %s gains %d gil and now has %d gil" % (char1.name, char2.name, char1.bounty, char2.wealth))
                print("You died, it's over, try again or go home")
                exit(0)

def Store(character):
    shopping = True
    while shopping: #while in the store
        items_dict = {'1':'SuperTonic', '2':'Armor', '3':'Cloak'}
        items_price_dict = { '1':5, '2':10, '3':20}
        
        print("%s has %d gold" % (character.name, character.wealth))#%s calls character.name #d calls character.wealth

        item = input("What do you want to buy?\n1. SuperTonic - 5g \n2. Armor - 10g\n3. Cloak -20g\n4. Quit\n:")
            #items that you can purchase
        if item == '4':
            shopping = False #if they put in number 4, you can't buy an item so 
        elif int(item) in [1,2,3] and character.wealth < items_price_dict[item] :
            print("%s can't afford this" % character.name)
            still_shopping = input("Continue shopping?\n1. Yes \n2. No \n: ")
            if still_shopping.lower() == "n" or still_shopping.lower() == "no" or still_shopping.lower() == "1":
                shopping = False
            elif still_shopping.lower() == "y"or still_shopping.lower() == "yes" or still_shopping.lower() == "2":
                pass
            else:
                print("You pressed the wrong key stupid, goodbye.")
                shopping = False 
        #so the n, no and 1
        elif int(item) in [1,2,3] and character.wealth >= items_price_dict[item]:
            character.wealth -= items_price_dict[item]
            character.inventory.append(items_dict[item])
            print("%s bought %s" % (character.name, items_dict[item]))
            still_shopping = input("Continue shopping?\n1. Yes \n2. No\n: ")
            if still_shopping.lower() == "n" or still_shopping.lower() == "no" or still_shopping.lower() =="2":
                shopping = False
            elif still_shopping.lower() == "y" or still_shopping.lower() == "yes" or still_shopping.lower() =="1":
                pass
            else:
                print("You pressed the wrong key stupid, goodbye.")
                shopping = False

        #so the store inputs, 1 2 or 3, for whichever item you want to buy or if you want to continue shopping with
        #1 and 2
        #The first half is being unable to purchase the items, the second is when you're able




def use_item(char1): #print the inventory of char1
    status = True
    while status: #in the menu
        print("What are you going to use?: ")
        for i,item in enumerate(char1.inventory): #enumerate keeps count of iterations
            print("%d. %s" %(i+1,item)) #start at 0 items, i+1 adds to inventory
        print("0. Quit") 
        request = int(input(":"))#int for the number of items
        print("")
        if request == 0:
            status = False #no items
        elif request <= len(char1.inventory) and request > 0:
            if char1.inventory[request-1] == "SuperTonic": #if you have supertonic, will show up here first
                char1.health += 10
                print("%s gained 10 health. You now have %d health" % (char1.name, char1.health))
            if char1.inventory[request-1] == "Armor":
                char1.armor += 2 #using armor adds +2
                print(" %s gains 2 armor. You now have %d armor." % (char1.name,char1.armor))
            if char1.inventory[request-1] == "Cloak": # request-1 subtracts from the inventory
                char1.evasion += 2
                print("%s gains 2 evasion. You now have %d evasion." % (char1.name, char1.evasion))
            del char1.inventory[request-1] #deletes out of inventory
            status = False

        else: print("Select something you have!") 

superboy = create_hero()
main(superboy)
from character import Character
from zombie import Zombie

"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""

def main():
    hero1 = Character("Sean",10, 5)
    goblin1 = Character("Gobbi",6,2) #un# so that you're able to fight something you can kill.
    #goblin1 = Zombie() #imported from zombie #un# so that you're able to fight something you can kill

    while goblin1.alive() and hero1.alive(): #using character code to attack.
        hero1.print_status() #return from character.py
        goblin1.print_status() #return from character.py
        print()
        print("What do you want to do?")
        print("1. fight %s" % goblin1.name)
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero1.attack(goblin1) #from the character.py
            if not goblin1.alive():
                print("The goblin is dead.")
        elif user_input == "2": #goblin still attacks
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin1.alive(): #from character.py
            # Goblin attacks hero
            goblin1.attack(hero1)
            if not hero1.alive(): #if you pass too many times, goblin will kill hero
                print("You are dead.")

main()

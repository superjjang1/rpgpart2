from character import *

"""
In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""

def main():
    char1 = Character('Sean','hero',10, 5)
    char2 = Character('Bob', 'jackie', 100, 1)

    while char2.alive() and char1.alive(): #using character code to attack.
        char1.print_status() #return from character.py
        char2.print_status() #return from character.py
        print()
        print("What do you want to do?")
        print("1. fight %s" % char2.name)
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            char1.attack(char2) #from the character.py
            if not char2.alive():
                print("The goblin is dead.")
        elif user_input == "2": #goblin still attacks
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if char2.alive(): #from character.py
            # Goblin attacks hero
            char2.attack(char1)
            if not char1.alive(): #if you pass too many times, goblin will kill hero
                print("You are dead.")

main()

#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee



class Character:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status_(self, name):
        self.name = name
        if self.name == "Hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.name == 'Goblin':
            print(f"The {self.name} has {self.power}.")
        else:
            print("Invalid Character Name")

class Hero(Character):
    
    def attack(self, goblin):
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))
        if goblin.health <= 0:
                print("The goblin is defeated.")


    # def alive(self):
    #     if self.health > 0:
    #         return True
    #     else:
    #         return False
        
    
    # def print_status_hero(self):
    #     print(f"You have {hero.health} health and {hero.power} power.")




class Goblin(Character):

    def attack(self, hero):
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
                print("You have been vanquished.")
    
    # def alive(self):
    #     if self.health > 0:
    #         return True
    #     else:
    #         return False

    def print_status_goblin(self):
        print(f"The goblin has {goblin.health} health and {goblin.power} power.")

hero = Hero("Hero", 10, 5)
goblin = Goblin("Goblin", 6, 2)











# def main():
#     hero_health = 10
#     hero_power = 5
#     goblin_health = 6
#     goblin_power = 2

#     while goblin_health > 0 and hero_health > 0:
#         print("You have {} health and {} power.".format(hero_health, hero_power))
#         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#             if hero_health <= 0:
#                 print("You are dead.")

# main()

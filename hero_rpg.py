#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random





class Character:
    def __init__(self, character_name, health, power):
        self.health = health
        self.power = power
        self.character_name = character_name

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        if enemy.character_name != "zombie" or "shadow":
            enemy.health -= self.power

        if self.character_name == "hero":
            double_damage = random.randint(1, 11)
            if double_damage > 8:
                enemy.health -= self.power
                print(f"You did double damage to the {enemy.character_name}")
            else:
                print(f"You do {self.power} damage to the {enemy.character_name}.")

        if enemy.character_name == "goblin":
            print(f"The {enemy.character_name} does {self.power} damage to you.")

        if enemy.character_name == "medic":
            print(f"The {enemy.name} does {enemy.power} damage to you.")
            recuperate = random.randint(1, 11)
            if recuperate > 8:
                enemy.health += 2
                print("The medic used a potion and recuperates 2 health points.")
            
        if enemy.character_name == "shadow":
            print(f"The {enemy.name} does {enemy.power} damage to you.")
            damage = random.randint(1, 11)
            if damage > 9:
                enemy.health -= self.power
            


    def print_status(self):
        if self.character_name == "hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "goblin":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "shadow":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "medic":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "zombie":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")



#CLASSES

class Hero(Character):
    def __init__(self, health, power):
        character_name = "hero"
        super(Hero, self).__init__(character_name, health, power)



class Enemy(Character):
    def __init__(self, name, health, power, bounty):
        self.name = name
        self.bounty = bounty
        super(Enemy, self).__init__(name, health, power)


class Goblin(Enemy):
    def __init__(self, health, power, bounty):
        character_name = "goblin"
        super(Goblin, self).__init__(character_name, health, power, bounty)


class Shadow(Enemy):
    def __init__(self, health, power, bounty):
        character_name = "shadow"
        super(Shadow, self).__init__(character_name, health, power, bounty)


class Medic(Enemy):
    def __init__(self, health, power, bounty):
        character_name = "medic"
        super(Medic, self).__init__(character_name, health, power, bounty)


class Zombie(Enemy):
    def __init__(self, health, power, bounty):
        character_name = "zombie"
        super(Zombie, self).__init__(character_name, health, power, bounty)


class Werewolf(Enemy):
    def __init__(self, health, power, bounty):
        character_name = "werewolf"
        super(Werewolf, self).__init__(character_name, health, power, bounty)



#GAME

hero = Hero(10, 5)
goblin = Goblin(6, 2, 5)
medic = Medic(6, 5, 5)
shadow = Shadow(1, 4, 8)
zombie = Zombie(6, 1, 10)

def main(enemy):
    


    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
            
            if not enemy.alive():
                print(f"The {enemy.name} is dead. You collect {enemy.bounty} bounty coins!")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.alive():
            enemy.attack(hero)
            
            if not hero.alive():
                print("You are dead.")

main(medic)
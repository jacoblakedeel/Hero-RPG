

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
        if enemy.character_name != "zombie":
            enemy.health -= self.power
        if enemy.character_name != "shadow":
            enemy.health -= self.power
        
        if self.character_name == "hero":
            if hero.armor > 0:
                hero.health += hero.armor
            double_damage = random.randint(1, 11)
            if double_damage > 8 and enemy.character_name != "zombie":
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
            

        if enemy.character_name == "thief":
            enemy.health -= hero.power
            hero.coins -= 1
            print(f"The {enemy.name} does {enemy.power} damage to you and stole one of your coins.")
            
            
        if enemy.character_name == "werewolf":
            enemy.health -= hero.power
            transformation = random.randint(1, 51)
            if transformation >= 45:
                hero.health = 0
                print("You have been transformed into a werewolf! GAME OVER!")
            
                
                


    def print_status(self):
        if self.character_name == "hero":
            print(f"You have {self.health} health, {self.power} power, {self.coins} coins, {self.armor} armor, and {self.evade} evade points.")
        elif self.character_name == "goblin":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "shadow":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "medic":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
        elif self.character_name == "zombie":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")



#CLASSES

class Items:
    def __init__(self, price):
        self.price = price
    
    def super_tonic(self):

        if hero.coins >= self.price:
            if hero.health < 15:
                hero.health = (15 - hero.health) + hero.health 
                hero.coins -= self.price
                hero.print_status
            else:
                print("You are already at maximum health")
        else:
            print("Not enough coins to purchase.")
            


class Hero(Character):
    def __init__(self, health, power, coins, armor, evade):
        character_name = "hero"
        self.health = health
        self.power = power
        self.coins = coins
        self.armor = armor
        self.evade = evade
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


class Thief(Enemy):
    def __init__(self, health, power, bounty):
        character_name = "thief"
        super(Thief, self).__init__(character_name, health, power, bounty)

#GAME

hero = Hero(15, 5, 5, 0, 0)
goblin = Goblin(8, 2, 5)
medic = Medic(10, 5, 5)
shadow = Shadow(1, 4, 8)
zombie = Zombie(1, 1, 10)
thief = Thief(15, 1, 10)
werewolf = Werewolf(20, 8, 20)

# store = Store()
super_tonic = Items(5)
armor = Items(5)
evade = Items(2)

def main(enemy):
    
    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. shop at the store")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
            hero.print_status
            enemy.print_status
            if not enemy.alive():
                hero.coins += enemy.bounty
                print(f"The {enemy.name} is dead. You collect {enemy.bounty} bounty coins!")
            if enemy.alive():
                enemy.attack(hero)
                if not hero.alive():
                    print("You are dead.")

        elif raw_input == "2":
            hero.health -= enemy.power
            print(f"The {enemy.character_name} did {enemy.power} damage to you")
        elif raw_input == "3":
            print("Choose Item From Store")
            print("=" * 20)
            print("1. Super Tonic - Restores Hero Health to 15. Price: 5 Coins")
            print("2. Armor - Adds 2 Armor Points. Price: 5 Coins")
            print("3. Evade - Makes Enemy Attacks Less Likely to Do Damage. Price: 2 Coins")
            print("4. Go back to main menu")
            print("")
            print("What would you like to purchase?")
            store_input = input()
            if store_input == "1":
                if hero.coins >= super_tonic.price:
                    if hero.health < 15:
                        hero.health = (15 - hero.health) + hero.health 
                        hero.coins -= super_tonic.price
                        hero.print_status
                        
                    else:
                        print("You are already at maximum health")
                else:
                    print("Not enough coins to purchase.")

            elif store_input == "2":
                if hero.coins >= armor.price:
                    hero.armor += 2
                    hero.coins -= armor.price
                    
                else:
                    print("Not enough coins to purchase.")
            elif store_input == "3":
                hero.evade += 2
                hero.coins -= 2
            elif store_input == "4":
                main(enemy)

        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        

main(shadow)
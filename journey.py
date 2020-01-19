#! python3
#journey.py is a text-based adventure game
import random
import time
from pprint import pprint

class Player(object):
    def __init__(self, Pname, Phealth, Pattack, Pdefense, Pranged, Pmagic):
        self.name = Pname
        self.health = Phealth
        self.attack = Pattack
        self.defense = Pdefense
        self.ranged = Pranged
        self.magic = Pmagic

    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getRanged(self):
        return self.ranged
    def getMagic(self):
        return self.magic

    def setName(self, newName):
        self.name = newName
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setDefense(self, newDefense):
        self.defense = newDefense
    def setRanged(self, newRanged):
        self.ranged = newRanged
    def setMagic(self, newMagic):
        self.magic = newMagic

    def pickup(self, input, item):
        if input == 'Y':
            self.inventory.append(item)
            return self.inventory
        elif input == 'N':
            return "All right. Let's get going."


def createClass():
    a = input("Are you more strategic(1) of more of a warrior(2)?...")
    while a != "1" and a != "2":
        print("invalid selection")
        a = input("Are you more strategic(1) of more of a warrior(2)?...")

    if a == "1":
        Pattack = 50
        Pdefense = 100
    elif a == "2":
        Pattack = 100
        Pdefense = 50

    b = input("Press enter to roll a dice.")
    time.sleep(0.2)
    print("Rolling dice...")
    playerLuck = random.randint(0,10)
    print(f"Your hero has {playerLuck} luck out of 10.")

    c = input("Bow and arrow(1) or magic(2)?")
    while c != "1" and c != "2":
        print("invalid selection")
        c = input("Bow and arrow(1) or magic(2)?")

    if c == "1":
        Pranged = 100
        Pmagic = 50
    elif c == "2":
        Pranged = 50
        Pmagic = 100

    Pname = input("What is your name hero?")
    print(f"Welcome {Pname}!!!")

    return (Pname, Pattack, Pdefense, Pranged, Pmagic)

class_data = createClass()

character = Player(100, class_data[0], class_data[1], class_data[2], class_data[3], class_data[4])

pprint(vars(character))

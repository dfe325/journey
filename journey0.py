#! python3

#journey.py is a text-based adventure game
#set in 1947 Los Angeles, you are a detective hired by an ingenue scientist to investigate
#whether or not her husband is having an affair.
#along the way, you will encounter nazi scientists, soviet spies, and maybe an
#alien or two as your investigation takes you from Tinsel Town to a secret
#government installation in the New Mexico desert known as the Indigo Zone.
#it will take all your wits to survive... so choose your adventure carefully!

name = input("What is your name, detective?\n")

def choice(options):
    print("Press ")
    for option in options:
        print(option)
    decision = input()

def decision(options, decision):
    print(decision)
    if decision in options:
        print(f"{decision} is a success!")

print(f"Los Angeles, 1947.\n Ever since returning from the war, you've \
kept a small office off of Wilshire Boulevard in the heart of Beverly Hills.\n\
Your specialty is suspicious spouses and snooping employers who \
suspect that their employees are secretly commies. It's not the most noble \
profession, but it's a living. \n\n \
So it's in your office, with the name Detective {name} written on the door, when \
you first come into contact with Mrs. Squires...")

print("A knock at the door. Will you answer it?")
options = ["Y", "N"]
choice(options)
decision(options, decision)

'''options = ["1", "2"]
print(f"Press {options[0]} to go in, {options[1]} to go back.")
choice(options)
decision(options, decision)'''

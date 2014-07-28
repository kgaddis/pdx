# Kainoa Gaddis (c) 2014
# Coin War assignment
# Instructions and rules are posted in moodle

"""
Outline

Two players

Each player starts out with five coins. make the initial lists for the hands

randomly flip each coin to show heads or tails
  * Randomly selet 1 or 0 and set 1 to Heads and 0 to Tails

maybe make a play menu
  * press enter to play or type 0 to exit

have both a prisoners list and an army list
  * remove the players at the front of the list when played and assign them to army lists or the prisoners list

run the playing loop and prints who wins


import tests from file
"""
from random import choice



def menu():
    print("\t\tWelcome to Coin War!\n")
    print("Main menu\n\t 0 to exit\n\t 1 to play")
 
### need play and menu in a while loop for break to work

def random_team():
    # Select random team
    team = []
    coin = ["H", "T"]
    for _ in range(5):
        i = choice(coin)
        team.append(i)
    return team

# I would make a new function in making teams from file inputs


def play():
    # Make initial teams
    army1 = random_team()
    army2 = random_team()
    prison1 = []
    prison2 = []

    print("Player 1: Army", "".join(army1))
    print("Player 2: Army", "".join(army2))
    input("Press Enter\n")

    # The actual playing loop
    while len(army1) > 0 and len(army2) > 0:
        if army1[0] == "H" and army2[0] == "T":
            army1.extend(["T", "H"])
            army1.extend(prison2)
            army1.extend(prison1)
            del army1[0], army2[0], prison1[:], prison2[:]
      
        elif army1[0] == "T" and army2[0] == "H":
            army2.extend(["T", "H"])
            army2.extend(prison1)
            army2.extend(prison2)
            del army1[0], army2[0], prison1[:], prison2[:]
      
        else:
            prison1.append(army1[0])
            prison2.append(army2[0])
            del army1[0]
            del army2[0]
            if army1 and army2:
                prison1.append(army1[0])
                prison2.append(army2[0])
                del army1[0]
                del army2[0]
      
        # Print to screen
        print("Player 1: Army", "".join(army1), "\tPrisoners", "".join(prison1))
        print("Player 2: Army", "".join(army2), "\tPrisoners", "".join( prison2))
       
        input("Press enter\n")


    # Display winner
    if len(army1) == 0 and len(army2) > 0:
        print("Player 2 wins!")
    elif len(army1) > 0 and len(army2) == 0:
        print("Player 1 wins!")
    elif prison1.count("H") > prison2.count("H"):
        print("Player 1 wins!")
    elif prison2.count("H") > prison1.count("H"):
        print("Player 2 wins!")
    else:
        print("Tie!")

# Main loop
menu()
i = None
while i not in ["0", "1"]:
    i = input("Choice: ")
    if i == "1":
        play()
    elif i == "0":
        print("Bye")
    else:
        print("Please select a valid option")


""" 

Put in read from file option

Also a set your team option

"""

# Kainoa Gaddis (c) 2014
# Flower Garden Take Home Final
# PSU New Beginnings


"""
Make initial garden
  - treat as list

set functions for each stage of development, idk if i need classes or not yet, thinking not

make animation function to use other development functions
  - this will also have the refresh and sleep timer stuff



"""
from time import sleep
from random import randrange

def display_garden():
    garden_str = "".join(g)
    print("  ", garden_str, end="\r")
     

def initial_garden(g):
    for i in range(60):
        g.append("_")
    g[30] = "."
    
    display_garden()
    return g


def prob(p):
    num = randrange(100)
    if num < p:
        return True
       
"""
def death(g):
    if prob(2):
        


def sprout():
    if prob(10):
        return ","
    else:
        return "."


def flower():
    if prob(10):
        return "*"
    else:
        return ","
"""

def update_garden(g):    
    for i in range(len(g)):
        if g[i] == ".":
            if prob(10):
                g[i] = ","

        elif g[i] == ",":
            if prob(10):
                g[i] = "*"

        elif g[i] == "*":
            if prob(2):
                g[i] = "_"

                num1 = randrange(i-5, i+6)
                num2 = randrange(i-5, i+6)
                while num2 == num1:
                    num2 = randrange(i-5, i+6)
                    
                new = [num1, num2]
                for j in new:
                    if j < 0 or j >= 60:
                        continue

                    if g[j] == "_":
                        g[j] = "."
 
    display_garden()
            
        
def animation(g):
    for i in range(720):
        sleep(1/24)
        update_garden(g)
    print()

# Main loop
g = []
initial_garden(g)
animation(g)
        

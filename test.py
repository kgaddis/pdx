# Kainoa Gaddis (c) 2014
# first repeadted element

import tkinter

def first_repeated(s):
    m = []
    for e in s:
        if e not in m:
            m.append(e)
        else:
            print(e)
            return e


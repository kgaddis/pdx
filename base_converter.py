# Kainoa Gaddis (c) 2014
# Base converter and quizzer

"""
This is a program that can convert numbers to binary and hexadecimal or vice versa


There will be two modes
    - Converter mode
    - Quiz mode

Converter mode should have user choose what they want to convert from and to
    - maybe use radial buttons and a entry box
    - Have a nice display that shows the input and output conversion

Quiz mode
    - can have different difficulties, beginner, medium, hard, custom

beginner can just be numbers to binary and vice versa

medium and hard can use hexidecimal and octadecimal as well

custom can have then select the number of bits, which bases they want to include, one way or both way\
time limit??, multiple choice or entry - im feeling entry, 

Probably need to make this with objects

Use a GUI, maybe try tkinter.ttk to use native look

Should i make it unlimited or a certain number or problems

maybe have a cheat sheet for the quizzes if needed that are the base answers

after the quiz can show results
    - how much correct
    - how long it took
    - average time per problem
    - maybe have a high scores list posted online if can **Extra

In each mode have a back button or main menu button to get back tot he main menu
"""

from tkinter import *
from tkinter import ttk

# Menu frame
class Menu(Frame):
    
    def __init__(self, master):
        super(Menu, self).__init__(master)
        self.grid()
        self.widgets()

    def widgets(self):
        
        Label(self, text = "This is a sample").grid(row = 0, column = 0)
        Button(self, text = "I do nothing").grid(row = 1, column = 0)

# Converter Frame


# Practice Quiz


# Converter game




# main function
def main():
    
    root = Tk()
    root.title("Base Number Converter")
    root.geometry("500x400+600+300")
    menu = Menu(root)
    root.mainloop()

# Run program
main()

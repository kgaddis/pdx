# Kainoa Gaddis (c) 2014
# Display die roll

from random import *
from tkinter import *
from tkinter.font import Font


class DieRoller(Frame):

    def __init__(self, root):
        super().__init__(root)
        self.grid()


        # Create widgets
        self.grid()
        dieFont = Font(size = 24)

        # Radio Buttons
        """
        self.number = StringVar()
        self.number.set(None)

        self.radio1 = Radiobutton(self, text = "One Dice", variable= self.number, value = "one")
        self.radio1.grid()
        self.radio2 = Radiobutton(self, text = "Two Die", variable= self.number, value = "two")
        self.radio1.grid()
        """

        # Labels
        self.die1 = Label(self, text = "Die 1").grid(row = 0, column = 0)
        self.die2 = Label(self, text = "Die 2").grid(row = 0, column = 2)
        self.summ = Label(self, text = "Sum").grid(row = 0, column = 4)
        self.display1 = Label(self, width = 2, font = dieFont)
        self.display1.grid(row = 1, column = 0, sticky = W)
        self.display2 = Label(self, width = 2,font = dieFont)
        self.display2.grid(row = 1, column = 2)
        self.summ_display = Label(self, width = 2, font = dieFont)
        self.summ_display.grid(row = 1, column = 4, sticky = E)

        # Button
        self.roll = Button(self, text = "Roll", command = self.do_roll)
        self.roll.grid(row = 2, column = 0, columnspan = 5, sticky = E + W)

    def rand_roll(self):
        roll = randrange(6) + 1
        return roll

    
    def do_roll(self):
        disp1 = self.rand_roll()
        disp2 = self.rand_roll()
        self.display1.configure(text = str(disp1))
        self.display2.configure(text = str(disp2))
        self.summ_display.configure(text = str(disp1 + disp2))


# Seed the PRNG
seed()


# Start the app
root = Tk()
root.title("Die Roller")
root.geometry("+500+300")

app = DieRoller(root)
root.mainloop()



"""
Add a second die with the same roll button
"""

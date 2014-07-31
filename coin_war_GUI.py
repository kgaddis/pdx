# Kainoa Gaddis (c) 2014
# Coin war assignment with GUI
# Instructions and rules are posted on moodle

from random import choice
from tkinter import *

class CoinWar(Frame):
    
    def __init__(self, root):
        super().__init__(root)
        self.grid()

        # Create Widgets
        # Intro
        Label(self, text = "Welcome to Coin War!").grid(column = 1)
        Label(self, text = "").grid(row = 1, column = 0)
        Label(self, text = "Choose method for generating teams").grid(row = 2, column = 0, columnspan = 3)
        
        # User team generation options
        self.random = Button(self, text ="Random", command = self.do_random)
        self.random.grid(row = 3, column = 0)
        self.text = Button(self, text = "Text File").grid(row = 3, column = 1)
        Label(self, text ="File name:").grid(row = 4, column = 1)
        self.text_box = Entry(self, width = 10).grid(row = 5, column = 1)
        self.usr_input = Button(self, text = "User Input", command = self.do_input)
        self.usr_input.grid(row = 3, column = 2, columnspan = 2, sticky = W)
        Label(self, text = "Player 1:").grid(row = 4, column = 2, sticky = W)
        Label(self, text = "Player 2:").grid(row = 5, column = 2, sticky = W)
        self.one_box = Entry(self, width = 7)
        self.one_box.grid(row = 4, column = 3, sticky = W)
        self.two_box = Entry(self, width = 7)
        self.two_box.grid(row = 5, column = 3, sticky = W)

        # The Display
        Label(self, text = "").grid(row = 6, column = 0)
        Label(self, text = "Player 1 -").grid(row = 7, column = 0, sticky = E)
        Label(self, text = "Player 2 -").grid(row = 8, column = 0, sticky = E)
        self.army1 = Label(self, text = "Army:")
        self.army1.grid(row = 7, column = 1, sticky = W)
        self.army2 = Label(self, text = "Army:")
        self.army2.grid(row = 8, column = 1, sticky = W)
        Label(self, text = "Prisoners:").grid(row = 7, column = 2, sticky = W)
        self.prison1 = Label(self)
        self.prison1.grid(row = 7, column = 3, sticky = W)
        Label(self, text = "Prisoners:").grid(row = 8, column = 2, sticky = W)
        self.prison2 = Label(self)
        self.prison2.grid(row = 8, column = 3, sticky = W)
 
        # Next Button and winner
        Label(self, text = "").grid(row = 9, column = 0)
        self.next_turn = Button(self, text = "Next Turn", command = self.do_next_turn)
        self.next_turn.grid(row = 10, column = 1)
        Label(self, text = "").grid(row = 11, column = 0)
        self.winner = Label(self)
        self.winner.grid(row = 12, column = 1, columnspan = 2)
        

    def random_team(self):
        # Select random team
        team = []
        coin = ["H", "T"]
        for _ in range(5):
            i = choice(coin)
            team.append(i)
        return team

    def do_random(self):
        # Make global values to be used with other methods
        global army1
        global army2
        global prison1
        global prison2
        
        # Make initial teams
        army1 = self.random_team()
        army2 = self.random_team()
        prison1 = []
        prison2 = []
        
        # Print and reset original values
        self.army1["text"] = "Army: " + "".join(army1)
        self.army2["text"] = "Army: " + "".join(army2)
        self.prison1["text"] = ""
        self.prison2["text"] = ""
        self.winner["text"] = ""
        self.next_turn["text"] = "Next Turn"

    def do_input(self):
        # Make global values to be used with other methods
        global army1
        global army2
        global prison1
        global prison2
        
        army1 = self.one_box.get()
        army2 = self.two_box.get()
        prison1 = []
        prison2 = []

     
        # Get correct input
        if len(army1) == 5 and len(army2) == 5:
            for i in army1:
                if i not in ["H", "T"]:
                    self.winner["text"] = "Please only type 'H' or 'T'"
                
                else:
                    for i in army2:
                        if i not in ["H", "T"]:
                            self.winner["text"] = "Please only type 'H' or 'T'"

                        else:
                            army1 = "".join(army1)
                            army2 = "".join(army2)

                            # Print and reset original values
                            self.army1["text"] = "Army: " + "".join(army1)
                            self.army2["text"] = "Army: " + "".join(army2)
                            self.prison1["text"] = ""
                            self.prison2["text"] = ""
                            self.winner["text"] = ""
                            self.next_turn["text"] = "Next Turn"                           

        else:
            self.winner["text"] = "You are only allowed 5 letters"

        # Put back into a list
        army1 = list(army1)
        army2 = list(army2)

        

    def do_next_turn(self):
        
        # The playing loop for one turn
        if len(army1) > 0 and len(army2) > 0:
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
                del army1[0], army2[0]
                if army1 and army2:
                    prison1.append(army1[0])
                    prison2.append(army2[0])
                    del army1[0], army2[0]

            # Print results after every turn
            self.army1["text"] = "Army: " + "".join(army1)
            self.army2["text"] = "Army: " + "".join(army2)
            self.prison1["text"] = "".join(prison1)
            self.prison2["text"] = "".join(prison2)



        # Display Winner 
        if len(army1) == 0 or len(army2) == 0:
            if len(army2) > len(army1):
                self.winner["text"] = "Player 2 wins!"
            elif len(army1) > len(army2):
                self.winner["text"] = "Player 1 wins!"
            elif prison1.count("H") > prison2.count("H"):
                self.winner["text"] = "Player 1 wins!"
            elif prison2.count("H") > prison1.count("H"):
                self.winner["text"] = "Player 2 wins!"
            else:
                self.winner["text"] = "Tie!"
            
            self.next_turn["text"] = "Game Over!"

# Start the app
root = Tk()
root.title("Coin War")
root.geometry("350x300+600+300")

app = CoinWar(root)
root.mainloop()



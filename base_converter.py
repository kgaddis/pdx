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
    - Use regular expressions to check input

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

for window setup i wnat to be able to find the display size and put my program in the middle of the screen
"""

from tkinter import *
from tkinter import ttk
import re

# Menu frame
class Menu(Frame):
    
    def __init__(self, master):
        super(Menu, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 7

    def widgets(self):
        
        self.titleframe = Frame(self, bd = 5)
        self.titleframe.grid(row = 0, column = 2, columnspan = 4)
        self.title1 = Label(self, text = "Welcome!", font = 16)
        self.title1.grid(row = 0, column = 2, columnspan = 1)
        self.title2 = Label(self, text = "Base Number Converter", font = 16)
        self.title2.grid(row = 1, column = 1, columnspan = 3)
        Label(self, text = "From").grid(row = 2, column = 1)
        Label(self, text = "To").grid(row = 2, column = 3)

        # Text box with from options
        self.text_in = Entry(self, width = 12)
        self.text_in.grid (row = 4, column = 0)
    
        self.entry = StringVar()
        self.entry.set(None)

        self.df_button = Radiobutton(self, text = "Decimal", variable = self.entry, value = "d")
        self.df_button.grid(row = 3, column = 1, sticky = W)
        self.bf_button = Radiobutton(self, text = "Binary", variable = self.entry, value = "b")
        self.bf_button.grid(row = 4, column = 1, sticky = W)
        self.hf_button = Radiobutton(self, text = "Hexadecimal", variable = self.entry, value = "h")
        self.hf_button.grid(row = 5, column = 1, sticky = W)
        
        # To options
        self.output = StringVar()
        self.output.set(None)
        
        self.dt_button = Radiobutton(self, text = "Decimal", variable = self.output, value = "d")
        self.dt_button.grid(row = 3, column = 3, sticky = W)
        self.bt_button = Radiobutton(self, text = "Binary", variable = self.output, value = "b")
        self.bt_button.grid(row = 4, column = 3, sticky = W)
        self.ht_button = Radiobutton(self, text = "Hexadecimal", variable = self.output, value = "h")
        self.ht_button.grid(row = 5, column = 3, sticky = W)
         
        # Convert Button and answer box
        self.conv_btn_frame = Frame(self, bd = 20)
        self.conv_btn_frame.grid(row = 7, column = 2)
        self.convert_btn = Button(self.conv_btn_frame, text = "Convert", command = self.disp_convert)
        self.convert_btn.grid()

        self.answer_frame1 = Frame(self, bd = 2, height = 50, width = 300, relief = "groove")
        self.answer_frame1.grid(row = 8, column = 1, columnspan = 3)
        self.answer_frame1.grid_propagate(0)
        self.answer_frame2 = Frame(self)
        self.answer_frame2.grid(row = 8, column = 1, columnspan = 3)
        self.answer = Label(self.answer_frame2, font = 12)
        self.answer.pack()


        # Lower Buttons
        self.practice_btn_frame = Frame(self, bd = 20)
        self.practice_btn_frame.grid(row = 9, column = 0, sticky = E)

        Button(self.practice_btn_frame, text = "Practice").grid()
        
        self.game_btn_frame = Frame(self, bd = 20)
        self.game_btn_frame.grid(row = 9, column = 4, sticky = E)

        Button(self.game_btn_frame, text = "Game").grid()

    def pretty_print(self, text, entry, output, answer):
        a = self.answer["text"] = text + " (" + entry +\
                     ") = " + answer + " (" + output + ")"
        return a

    def error_print(self):
        a = self.answer["text"] = "Error: Invalid input for this conversion"
    def convert_d_b(self, text):
       
        # Calculations
        num = int(text)
        converted_num = ""
        while num != 0:
            R = num % 2
            converted_num = str(R) + converted_num

            D = num // 2
            num = D
        
        answer = self.pretty_print(text, "d", "b", converted_num)
        return answer
        

    def convert_d_h(self, text): 
        
        # Calculations
        num = int(text)
        converted_num = ""
        while num != 0:
            R = num % 16
            if R == 10:
                R = "a"
            elif R == 11:
                R = "b"
            elif R == 12:
                R = "c"
            elif R == 13:
                R = "d"
            elif R == 14:
                R = "e"
            elif R == 15:
                R = "f"

            converted_num = str(R) + converted_num

            D = num // 16
            num = D
        
        answer = self.pretty_print(text, "d", "h", converted_num)
        return answer

    def convert_b_d(self, text):
        # Calculate
        n = 0
        text_list = list(text)
        converted_num = 0
        while text_list != []:
            converted_num += (2 ** n) * int(text_list[-1])
            del text_list[-1]
            n += 1
        
        answer = self.pretty_print(text, "b", "d", str( converted_num))
        return answer

    def disp_convert(self):
        
        entry = self.entry.get()
        output = self.output.get()
        text = self.text_in.get()

        
        # If not entry in textbox
        if text == "":
            self.answer["text"] = "No entry in textbox"
        
        # If no selection
        elif entry == "None" or output == "None":
            self.answer["text"] = "Please select conversion types"
                
        # If they are the same
        elif entry == output:
            self.answer["text"] = text + " (" + entry + ") = "\
                 + text + " (" + output + ")"

        # dec to bin using right to left method
        elif entry == "d" and output == "b":
            regex = re.compile("[0-9]+")
            result = regex.fullmatch(text)
            
            if result != None:
                self.convert_d_b(text)
            else:
                self.error_print()
            
        # dec to hex    
        elif entry == "d" and output == "h":
            regex = re.compile("[0-9]+")
            result = regex.fullmatch(text)
            
            if result != None:
                self.convert_d_h(text)
            else:
                self.error_print()
         
        # bin to dec
        elif entry == "b" and output == "d":
            regex = re.compile("[01]+")
            result = regex.fullmatch(text)
         
            if result != None:
                self.convert_b_d(text)
            else:
                self.error_print()
         
         
        # bin to hex
        elif entry == "b" and output == "h":
            self.answer["text"] = "binary to hex"
        
        # hex to dec
        elif entry == "h" and output == "d":
            regex = re.compile("[0-9a-fA-F]+")
            result = regex.fullmatch(text)
            
            self.answer["text"] = "hex to decimal"
        
        # hex to bin
        elif entry == "h" and output == "b":
            self.answer["text"] = "hex to binary"
        

        # Delete entry box
        #self.text_in.delete(0, END) 

                

    def change(self):
        return Practice(root)
# Converter Frame


# Practice Quiz
class Practice(Frame):
    
    def __init__(self, master):
        super(Practice, self).__init__(master)
        self.grid()
        self.widgets()

    def widgets(self):
        Label(self, text = "Practice").grid(row = 0, column = 3)
        
# Converter game




# main function
def main():
    
    root = Tk()
    root.title("Base Number Converter")
    root.geometry("560x350+600+300")
    screen = Menu(root)
    root.mainloop()

# Run program
main()

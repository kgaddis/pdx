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
import re

# Menu frame
class Menu(Frame):
    
    def __init__(self, master):
        super(Menu, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 7
    

    def widgets(self):
        
        self.title1 = Label(self, text = "Welcome!", font = ("Helvetica", 28))
        self.title1.grid(row = 0, column = 1, columnspan = 3)
        self.title2 = Label(self, text = "Base Number Converter", font = ("Helvetica", 24), pady = 8)
        self.title2.grid(row = 1, column = 1, columnspan = 3)
        Label(self, text = "From", font = ("Helvetica", 10, "underline")).grid(row = 2, column = 1)
        Label(self, text = "To", font = ("Helvetica", 10, "underline")).grid(row = 2, column = 3)

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

        self.answer_frame1 = Frame(self, bd = 2, height = 50, width = 350, relief = "groove")
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

    def same(self, text, entry, output):
        a = self.answer["text"] = text + " (" + entry + ") = "\
                 + text + " (" + output + ")"
        return a
        
    def error_print(self):
        a = self.answer["text"] = "Error: Invalid input for this conversion"
        
        return a
        
    def convert_d_b(self, text):
       
        # Calculations
        num = int(text)
        converted_num = ""
        while num != 0:
            R = num % 2
            converted_num = str(R) + converted_num

            D = num // 2
            num = D
        
        return converted_num
        

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
        
        return converted_num
        
    def convert_b_d(self, text):

        # Calculations
        n = 0
        text_list = list(text)
        converted_num = 0
        while text_list != []:
            converted_num += (2 ** n) * int(text_list[-1])
            del text_list[-1]
            n += 1
        
        return str(converted_num)
        
    def convert_h_d(self, text):
        
        # Calculations
        n = 0
        text_list = list(text)
        text_list = [i.replace("a", "10") for i in text_list]
        text_list = [i.replace("b", "11") for i in text_list]
        text_list = [i.replace("c", "12") for i in text_list]
        text_list = [i.replace("d", "13") for i in text_list]
        text_list = [i.replace("e", "14") for i in text_list]
        text_list = [i.replace('f', "15") for i in text_list]
        
        converted_num = 0
        while text_list != []:
            converted_num += (16 ** n) * int(text_list[-1])
            del text_list[-1]
            n += 1
        
        return str(converted_num)
        

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
                
       
        # decimal input
        elif entry == "d":
            regex = re.compile("[0-9]+")
            result = regex.fullmatch(text)
            
            if result != None:
                # to binary
                if output == "b":
                    answer = self.convert_d_b(text)
                    self.pretty_print(text, entry, output, answer)
                # to hexadeciaml
                elif output == "h":
                    answer = self.convert_d_h(text)
                    self.pretty_print(text, entry, output, answer)
                # to deccimal
                elif output == "d":
                    self.same(text, entry, output)
                
            else:
                self.error_print()
            
            
        # binary input
        elif entry == "b":
            regex = re.compile("[01]+")
            result = regex.fullmatch(text)    

            if result != None:
                # to decimal
                if output == "d":
                    answer = self.convert_b_d(text)
                    self.pretty_print(text, entry, output, answer)
                # to hexadecimal    
                elif output == "h":
                    answer = self.convert_d_h(self.convert_b_d(text))
                    self.pretty_print(text, entry, output, answer)
                # to binary
                elif output == "b":
                    self.same(text, entry, output)
                
            else:
                self.error_print()
         

        # hexadecimal input
        elif entry == "h":
            regex = re.compile("[0-9a-f]+")
            result = regex.fullmatch(text)
            
            if result != None:
                # to decimal
                if output == "d":
                    answer = self.convert_h_d(text)
                    self.pretty_print(text, entry, output, answer)
                # to binary    
                elif output == "b":
                    answer = self.convert_d_b(self.convert_h_d(text))
                    self.pretty_print(text, entry, output, answer)
                # to hexadecimal
                elif output == "h":
                    self.same(text, entry, output)
                
            else:
                self.error_print()
         
        
    #def change(self):
        #return Practice(root)

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
    
    # Get screenheight and screenwidth of monitor being used to place app in center
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    
    # Calculate offset
    sw = screenwidth // 2 - 585 // 2
    sh = screenheight // 2 - 410 // 2
    
    root.geometry("585x410+" + str(sw) + "+" + str(sh))
    
    screen = Menu(root)
    root.mainloop()

# Run program
main()

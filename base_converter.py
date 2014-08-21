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
import random

u_font = ("Helvetica", 10, "underline")
t_font = ("Helvetica", 28)

# Menu frame
class Converter(Frame):
    
    def __init__(self, master):
        super(Converter, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 7
    

    def widgets(self):
        
        self.title1 = Label(self, text = "Welcome!", font = t_font)
        self.title1.grid(row = 0, column = 1, columnspan = 3)
        self.title2 = Label(self, text = "Base Number Converter", font = ("Helvetica", 24), pady = 8)
        self.title2.grid(row = 1, column = 1, columnspan = 3)
        Label(self, text = "From", font = u_font).grid(row = 2, column = 1)
        Label(self, text = "To", font = u_font).grid(row = 2, column = 3)

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
        self.conv_btn_frame = Frame(self, pady = 20, padx = 20)
        self.conv_btn_frame.grid(row = 7, column = 2)
        self.convert_btn = Button(self.conv_btn_frame, text = "Convert", command = self.disp_convert)
        self.convert_btn.grid()

        self.answer_frame1 = Frame(self, bd = 2, height = 50, width = 350, relief = "groove")
        self.answer_frame1.grid(row = 8, column = 1, columnspan = 3)
        self.answer_frame1.grid_propagate(0)
        self.answer_frame2 = Frame(self)
        self.answer_frame2.grid(row = 8, column = 1, columnspan = 3)
        self.answer = Label(self.answer_frame2, font = 12)
        self.answer.grid()


        # Lower Buttons
        self.practice_btn_frame = Frame(self, pady = 20, padx = 20)
        self.practice_btn_frame.grid(row = 9, column = 0, sticky = E)

        Button(self.practice_btn_frame, text = "Practice", command = self.go_practice).grid()
        
        self.game_btn_frame = Frame(self, pady = 20, padx = 20)
        self.game_btn_frame.grid(row = 9, column = 4, sticky = E)

        Button(self.game_btn_frame, text = "Game", command = self.go_game).grid()

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
         
    def go_practice(self):
        self.destroy()
        return Practice_Menu(root)

    def go_game(self):
        self.destroy()
        return Game_Menu(root)

class Question(Converter):
    # Question class to be used with practice and game classes

    def __init__(self, master, diff):
        self.diff = diff
        self.create_question()
        self.ans()
        #print(self.question)
        #print(self.answer)

    def ans(self):
        ans_list = self.question.split()
        text = ans_list[0]
        if ans_list[1] == "(d)":
            if ans_list[3] == "(b)":
                self.answer = self.convert_d_b(text)
            elif ans_list[3] == "(h)":
                self.answer = self.convert_d_h(text)
        elif ans_list[1] == "(b)":
            if ans_list[3] == "(d)":
                self.answer = self.convert_b_d(text)
            elif ans_list[3] == "(h)":
                self.answer = self.convert_d_h(self.convert_b_d(text))
        elif ans_list[1] == '(h)':
            if ans_list[3] == "(d)":
                self.answer = self.convert_h_d(text)
            elif ans_list[3] == "(b)":
                self.answer = self.convert_d_b(self.convert_h_d(text))
        
            

    def create_question(self):
        # Makes a single question
        if self.diff == "e":
            c = random.choice(["d", "b"])
            num = str(random.randrange(2,16))
            
            if c == "d":
                self.question = num + " (d)  to  (b)"
            elif c == "b":
                self.question = self.convert_d_b(num) + " (b)  to  (d)" 
                
        elif self.diff == "m":
            converts = ["d", "b", "h"]
            c = random.choice(converts)
            converts.remove(c)

            num = str(random.randrange(2, 64))
            
            if c == "d":
                out = random.choice(converts)
                self.question = num + " (d)  to  (" + out +")"
            elif c == "b":
                out = random.choice(converts)
                self.question = self.convert_d_b(num) + " (b)  to  (" + out +")" 
            elif c == "h":
                out = random.choice(converts)
                self.question = self.convert_d_h(num) + " (h)  to  (" + out +")"

        elif self.diff == "h":
            converts = ["d", "b", "h"]
            c = random.choice(converts)
            converts.remove(c)

            num = str(random.randrange(2, 512))

            if c == "d":
                out = random.choice(converts)
                self.question = num + " (d)  to  (" + out +")"
            elif c == "b":
                out = random.choice(converts)
                self.question = self.convert_d_b(num) + " (b)  to  (" + out +")" 
            elif c == "h":
                out = random.choice(converts)
                self.question = self.convert_d_h(num) + " (h)  to  (" + out +")"

                
# Practice Quiz
class Practice_Menu(Frame):
    
    def __init__(self, master):
        super(Practice_Menu, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 7


    def widgets(self):
        # Title and instructions
        Label(self, text = "Base Converter\nPractice", font = t_font).grid(row = 0, column = 2)

        self.inst_list = []
        for i in range(6):
            self.inst_list.append(Label(self))
            self.inst_list[i].grid(row = i + 1, column = 1, columnspan = 3, sticky =  W)
        
        self.inst_list[0]["text"] = "You have heard the espression 'practice makes perfect'."
        self.inst_list[1]["text"] += "Here is where you can practice your base conversion skills."
        self.inst_list[2]["text"] += "There are three difficulties you can select from."
        self.inst_list[3]["text"] += "You will be given ten problems with no time limit."
        self.inst_list[4]["text"] += "Enter the correct answer in the associated textbox."
        self.inst_list[5]["text"] += "Click submit when finished."


        # Difficulty options
        self.diff = StringVar()
        self.diff.set(None)

        self.diff_frame = Frame(self, pady = 20, padx = 20)
        self.diff_frame.grid(row = 7, column = 2)
        
        self.easy = Radiobutton(self.diff_frame, variable = self.diff, value = "e")
        self.easy["text"] = "Easy - decimal and binary"
        self.easy.grid(row = 0, column = 2, sticky = W)
        self.medium = Radiobutton(self.diff_frame, variable = self.diff, value = "m")
        self.medium["text"] = "Medium - decimal, binary and hexadecimal"
        self.medium.grid(row = 1, column = 2, sticky = W)
        self.hard = Radiobutton(self.diff_frame, variable = self.diff, value = "h")
        self.hard["text"] = "Hard - larger decimal, binary and hexadecimal"
        self.hard.grid(row = 2, column = 2, sticky = W)
        
        # Buttons
        self.back_btn_frame = Frame(self, pady = 20, padx = 20)
        self.back_btn_frame.grid(row = 8, column = 0, sticky = E)

        Button(self.back_btn_frame, text = "Back", command = self.back).grid()

        self.begin_btn_frame = Frame(self, pady = 20, padx = 20)
        self.begin_btn_frame.grid(row = 8, column = 4, sticky = E)

        Button(self.begin_btn_frame, text = "Begin", command = self.begin).grid(row = 5, column = 4)
        
        self.error_label = Label(self, font = 12)
        self.error_label.grid(row = 8, column = 2)
        
    def back(self):
        self.destroy()
        return Converter(root)

    def begin(self):
        if self.diff.get() != "None":
            self.destroy()
            return Practice(root, self.diff.get())
        else:
            self.error_label["text"] = "Please select a difficulty."
            
class Practice(Converter):
    
    def __init__(self, master, diff):
        super(Practice, self).__init__(master)
        self.grid()
        self.widgets()
        self.diff = diff
        self.quiz()
        #print(self.diff)
        
    def widgets(self):
        self.title = Label(self, text = "Convert", font = t_font)
        self.title.grid(row = 0, column = 1, columnspan = 3)
        self.subtitle = Label(self, text = "d - decimal : b - binary : h - hexadecimal")
        self.subtitle.grid(row = 1, column = 0, columnspan = 5)

        self.question_list = []
        self.entry_box_list = []
        self.answer_list = []
        for i in range(10):
            self.question_list.append(Label(self, pady = 4))
            self.question_list[i].grid(row = i + 2, column = 0, sticky = W)
            self.entry_box_list.append(Entry(self, width = 10))
            self.entry_box_list[i].grid(row = i + 2, column = 2, sticky = E)
       
        # Buttons
        self.quit_btn_frame = Frame(self, pady = 20, padx = 50)
        self.quit_btn_frame.grid(row = 12, column = 0, sticky = W)

        Button(self.quit_btn_frame, text = "Quit", command = self.menu).grid()

        self.submit_btn_frame = Frame(self, pady = 20, padx = 50)
        self.submit_btn_frame.grid(row = 12, column = 4, sticky = W)

        Button(self.submit_btn_frame, text = "Submit", command = self.submit).grid()

        self.cheat_btn_frame = Frame(self, padx = 0)
        self.cheat_btn_frame.grid(row = 2, column = 4, columnspan = 2, sticky = W)

        self.cheat_btn = Button(self.cheat_btn_frame, text = "Cheat Sheet", command = self.cheat)
        self.cheat_btn.grid()

        self.error_label = Label(self, font = 12)
        self.error_label.grid(row = 12, column = 0, columnspan = 5)
        

    def quiz(self):
        q_list = []
        for i in range(10):
            while True:
                obj = Question(root, self.diff)
                q = obj.question
                if q in q_list:
                    continue
                else:
                    self.question_list[i]["text"] = str(i + 1) + ".\t" +  q
                    q_list.append(q)
                    self.answer_list.append(obj.answer)
                    break
        
        
    def cheat(self):
        if self.cheat_btn["text"] == "Cheat Sheet":
        
            self.cheat_frame = Frame(self, bd = 2, relief = "flat")
            self.cheat_frame.grid(row = 3,  column = 4, rowspan = 9, columnspan = 2, sticky = W)

            Label(self.cheat_frame, text = "Binary", font = u_font).grid(row = 0)

            self.cheat_list_b = []
            for i in range(6):
                self.cheat_list_b.append(Label(self.cheat_frame))
                self.cheat_list_b[i].grid(row = i + 1, sticky = W)

            for i in range(5):
                self.cheat_list_b[i]["text"] = "2^"+str(i)+" = "+str(2 ** i)+"\t\t 2^"+str(i+5)+" = "+str(2 ** (i + 5)) 

            Label(self.cheat_frame, text = "Decimal\t\tHexadecimal", font = u_font).grid(row = 7)

            self.cheat_list_dh = []
            for i in range(3):
                self.cheat_list_dh.append(Label(self.cheat_frame))
                self.cheat_list_dh[i].grid(row = i + 8, sticky = W)

            num_list = [1, 10, 100, 1, 16, 256] 
            for i in range(3):
                self.cheat_list_dh[i]["text"] = "10^"+str(i)+" = "+str(10 ** i)+" \t16^"+str(i)+" = "+str(16 ** i) 

            self.cheat_btn["text"] = "Close Cheat Sheet"

        else:
            self.cheat_btn["text"] = "Cheat Sheet"
            self.cheat_frame.destroy()

    
    def menu(self):
        self.destroy()
        return Converter(root)


    def submit(self):
        self.entry_list = []
        for i in range(10):
            if self.entry_box_list[i].get() == "":
                err = self.error_label["text"] = "Please answer all questions."
                return err
            else:
                self.entry_list.append(self.entry_box_list[i].get())
        
        self.q_and_a = []
        for i in range(10):
            self.q_and_a.append([self.question_list[i]["text"], self.entry_list[i], self.answer_list[i]])
        self.destroy()
        return Practice_Score(root, self.q_and_a)
            



class Practice_Score(Frame):
    
    def __init__(self, master, data):
        super(Practice_Score, self).__init__(master)
        self.grid()
        self.data = data
        self.widgets()
        self["borderwidth"] = 7

    def widgets(self):
        self.title = Label(self, text = "Score", font = t_font)
        self.title.grid(row = 0, column = 0, columnspan = 5)
        self.subtitle = Label(self, font = ("Helvetica", 16))
        self.subtitle.grid(row = 1, column = 0, columnspan = 5)

        Label(self, text = "Question", font = u_font).grid(row = 2, column = 0)
        Label(self, text = "Your Answer", font = u_font, padx = 20).grid(row = 2, column = 1)
        Label(self, text = "Corrext Answer", font = u_font, padx = 5).grid(row = 2, column = 2)
        Label(self, text = "Result", font = u_font, padx = 20).grid(row = 2, column = 3)
        
        self.question = []
        self.yours = []
        self.correct = []
        self.result = []
        self.score = 0
        for i in range(10):
            self.question.append(Label(self, text = self.data[i][0], padx = 4, pady = 3))
            self.question[i].grid(row = i + 3, column = 0, sticky = W)
            
            self.yours.append(Label(self, text = self.data[i][1]))
            self.yours[i].grid(row = i + 3, column = 1)
            
            self.correct.append(Label(self, text = self.data[i][2]))
            self.correct[i].grid(row = i + 3, column = 2)

            self.result.append(Label(self))
            self.result[i].grid(row = i + 3, column = 3)

            if self.data[i][1] == self.data[i][2]:
                self.result[i]["text"] = "Correct"
                self.score += 1
            else:
                self.result[i]["text"] = "Wrong"
            
        self.subtitle["text"] = str(self.score) + "/10"
        
        # Buttons
        self.menu_btn_frame = Frame(self, pady = 20, padx = 20)
        self.menu_btn_frame.grid(row = 13, column = 0)

        Button(self.menu_btn_frame, text = "Menu", command = self.menu).grid()

        self.trya_btn_frame = Frame(self, pady = 20, padx = 20)
        self.trya_btn_frame.grid(row = 13, column = 3, sticky = E)

        Button(self.trya_btn_frame, text = "Try Again", command = self.trya).grid()
        
        self.print_label = Label(self, font = 12)
        self.print_label.grid(row = 13, column = 1, columnspan = 2)
        if self.score == 10:
            self.print_label["text"] = "Perfect!"
        elif self.score >= 8:
            self.print_label["text"] = "Well Done!"
        elif self.score >= 6:
            self.print_label["text"] = "Above Average"
        elif self.score >= 4:
            self.print_label["text"] = "Can do better"
        else:
            self.print_label["text"] = "You need more practice"
    
    def compare(self):
        print(self.data[0])
    

    def menu(self):
        self.destroy()
        return Converter(root)

    def trya(self):
        self.destroy()
        return Practice_Menu(root)



# Converter game
class Game_Menu(Frame):
    def __init__(self, master):
        super(Game_Menu, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 7

    def widgets(self):
        # Title and instructions
        Label(self, text = "Base Converter\nGame", font = t_font).grid(row = 0, column = 2)

        self.inst_list = []
        for i in range(6):
            self.inst_list.append(Label(self))
            self.inst_list[i].grid(row = i + 1, column = 1, columnspan = 3, sticky =  W)
        
        self.inst_list[0]["text"] = "You have heard the espression 'practice makes perfect'."
        self.inst_list[1]["text"] += "Here is where you can practice your base conversion skills."
        self.inst_list[2]["text"] += "There are three difficulties you can select from."
        self.inst_list[3]["text"] += "You will be given ten problems with no time limit."
        self.inst_list[4]["text"] += "Enter the correct answer in the associated textbox."
        self.inst_list[5]["text"] += "Click submit when finished."


        # Difficulty options
        self.diff = StringVar()
        self.diff.set(None)

        self.diff_frame = Frame(self, pady = 20, padx = 20)
        self.diff_frame.grid(row = 7, column = 2)
        
        self.easy = Radiobutton(self.diff_frame, variable = self.diff, value = "e")
        self.easy["text"] = "Easy - decimal and binary"
        self.easy.grid(row = 0, column = 2, sticky = W)
        self.medium = Radiobutton(self.diff_frame, variable = self.diff, value = "m")
        self.medium["text"] = "Medium - decimal, binary and hexadecimal"
        self.medium.grid(row = 1, column = 2, sticky = W)
        self.hard = Radiobutton(self.diff_frame, variable = self.diff, value = "h")
        self.hard["text"] = "Hard - larger decimal, binary and hexadecimal"
        self.hard.grid(row = 2, column = 2, sticky = W)
        
        # Low Buttons
        self.back_btn_frame = Frame(self, pady = 20, padx = 20)
        self.back_btn_frame.grid(row = 8, column = 0, sticky = E)

        Button(self.back_btn_frame, text = "Back", command = self.back).grid()

        self.play_btn_frame = Frame(self, pady = 20, padx = 20)
        self.play_btn_frame.grid(row = 8, column = 4, sticky = E)

        Button(self.play_btn_frame, text = "Play", command = self.play).grid()
        
        self.error_label = Label(self, font = 12)
        self.error_label.grid(row = 8, column = 2)
        
    def back(self):
        self.destroy()
        return Converter(root)

    def play(self):
        if self.diff.get() != "None":
            self.destroy()
            return Game(root, self.diff.get())
        else:
            self.error_label["text"] = "Please select a difficulty."
    
class Game(Converter):
    
    def __init__(self, master, diff):
        super(Game, self).__init__(master)
        self.grid()
        self.widgets()
        self.diff = diff
        print(self.diff)
        
    def widgets(self):
        Label(self, text = "This is the game area").grid(row = 0)
        Button(self, text = "Menu", command = self.menu).grid(row = 5, column = 0)

    def menu(self):
        self.destroy()
        return Converter(root)



# main function

root = Tk()
root.title("Base Number Converter")

# Get screenheight and screenwidth of monitor being used to place app in center
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

# Calculate offset
sw = screenwidth // 2 - 585 // 2
sh = screenheight // 2 - 410 // 2

root.geometry("585x410+" + str(sw) + "+" + str(sh))

screen = Converter(root)
root.mainloop()


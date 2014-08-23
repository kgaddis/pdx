# Kainoa Gaddis (c) 2014
# This is a project for PSU New Beginning Program
# Base Converter, Practice, and Game
# This program is a base converter that can convert numbers between decimal, binary, and hexadecimal
# The user can also practice their skills with an untimed quiz
# The user can also play a game to answe as many conversions as possible in 1 minute


from tkinter import *
import re
import random

# Font to be used later
u_font = ("Helvetica", 10, "underline")
t_font = ("Helvetica", 28)


class Converter(Frame):
    # Menu and Converter frame

    def __init__(self, master):
        super(Converter, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 7
    

    def widgets(self):
        # Titles and stationary lables
        self.title1 = Label(self, text = "Welcome!", font = t_font)
        self.title1.grid(row = 0, column = 1, columnspan = 3)
        self.title2 = Label(self, text = "Base Number Converter", font = ("Helvetica", 24), pady = 8)
        self.title2.grid(row = 1, column = 1, columnspan = 3)
        Label(self, text = "From", font = u_font).grid(row = 2, column = 1)
        Label(self, text = "To", font = u_font).grid(row = 2, column = 3)

        # Text box with convert "from" radio buttons
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
        
        # Convert "To" radio buttons
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

        # Multiple stacked frames to make frame outline
        self.answer_frame1 = Frame(self, bd = 2, height = 50, width = 350, relief = "groove")
        self.answer_frame1.grid(row = 8, column = 1, columnspan = 3)
        self.answer_frame1.grid_propagate(0)
        self.answer_frame2 = Frame(self)
        self.answer_frame2.grid(row = 8, column = 1, columnspan = 3)
        self.answer = Label(self.answer_frame2, font = 12)
        self.answer.grid()

        # Lower Practice and Game Buttons
        self.practice_btn_frame = Frame(self, pady = 20, padx = 20)
        self.practice_btn_frame.grid(row = 9, column = 0, sticky = E)
        Button(self.practice_btn_frame, text = "Practice", command = self.go_practice).grid()
        
        self.game_btn_frame = Frame(self, pady = 20, padx = 20)
        self.game_btn_frame.grid(row = 9, column = 4, sticky = E)
        Button(self.game_btn_frame, text = "Game", command = self.go_game).grid()

    
    def pretty_print(self, text, entry, output, answer):
        # Method to make answer look nice
        a = self.answer["text"] = text + " (" + entry +\
                                 ") = " + answer + " (" + output + ")"
        return a


    def same(self, text, entry, output):
        # Method to use if the from and to buttons are the same, eg. both decimal
        a = self.answer["text"] = text + " (" + entry + ") = "\
                                 + text + " (" + output + ")"
        return a

        
    def error_print(self):
        # print if the input is invalid
        a = self.answer["text"] = "Error: Invalid input for this conversion"
        return a

        
    def convert_d_b(self, text):
        # Calculations for decimal to binary conversion
        num = int(text)
        converted_num = ""
        while num != 0:
            R = num % 2
            converted_num = str(R) + converted_num

            D = num // 2
            num = D
        
        return converted_num


    def convert_d_h(self, text): 
        # Calculations for decimal to hexadecimal conversion
        num = int(text)
        converted_num = ""
        while num != 0:
            R = num % 16
            # Change double digit values to their letter form
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
        # Calculations for binary to decimal conversion
        n = 0
        text_list = list(text)
        converted_num = 0
        while text_list != []:
            converted_num += (2 ** n) * int(text_list[-1])
            del text_list[-1]
            n += 1
        
        return str(converted_num)

        
    def convert_h_d(self, text):
        # Calculations for hexadecimal to decimal conversion
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
                     
        # If decimal input
        elif entry == "d":
            # Use regular expressions to get a valid input
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
                # to decimal
                elif output == "d":
                    self.same(text, entry, output)
            else:
                self.error_print()
                        
        # If binary input
        elif entry == "b":
            # Use regular expressions to get a valid input
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
         
        # If hexadecimal input
        elif entry == "h":
            # Use regular expressions to get a valid input
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
        # When Practice button clicked
        # Destroyes the converter frame and makes a practice menu frame
        self.destroy()
        return Practice_Menu(root)

    def go_game(self):
        # When Game button clicked
        # Destroyes the converter frame and makes a game menu frame
        self.destroy()
        return Game_Menu(root)

class Question(Converter):
    # Question class to be used with practice and game classes
    # Child of converter class
    # It makes a single question and answer pair

    def __init__(self, master, diff):
        self.diff = diff
        self.create_question()
        self.ans()


    def ans(self):
        # Solves te answer to self.question
        ans_list = self.question.split()
        text = ans_list[0]
        
        # Uses the conversions from the Converter class
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
        # Makes a single random question

        # If difficulty if easy
        if self.diff == "e":
            c = random.choice(["d", "b"])

            # Easy chooses random numbers from 2 to 16
            num = str(random.randrange(2,16))
            
            if c == "d":
                self.question = num + " (d)  to  (b)"
            elif c == "b":
                self.question = self.convert_d_b(num) + " (b)  to  (d)" 
        
        # If difficulty is medium
        elif self.diff == "m":
            converts = ["d", "b", "h"]
            c = random.choice(converts)
            # remove to output is one of the other choices
            converts.remove(c)

            # Medium chooses random numbers from 2 to 64
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

        # If difficulty is hard
        elif self.diff == "h":
            converts = ["d", "b", "h"]
            c = random.choice(converts)
            # remove to output is one of the other choices
            converts.remove(c)

            # Hard chooses random numbers from 2 to 512
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

                
class Practice_Menu(Frame):
    # Menu for the practice Quiz

    def __init__(self, master):
        super(Practice_Menu, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 7


    def widgets(self):
        # Title and instructions
        Label(self, text = "Base Converter\nPractice", font = t_font).grid(row = 0, column = 2)

        # Used for loop to make 6 labels quickly
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

        # Difficulty options using radiobuttons
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
        
        # Back and Begin Buttons
        self.back_btn_frame = Frame(self, pady = 20, padx = 20)
        self.back_btn_frame.grid(row = 8, column = 0, sticky = E)
        Button(self.back_btn_frame, text = "Back", command = self.back).grid()

        self.begin_btn_frame = Frame(self, pady = 20, padx = 20)
        self.begin_btn_frame.grid(row = 8, column = 4, sticky = E)
        Button(self.begin_btn_frame, text = "Begin", command = self.begin).grid(row = 5, column = 4)
        
        # Error label
        self.error_label = Label(self, font = 12)
        self.error_label.grid(row = 8, column = 2)
        

    def back(self):
        # Takes program back to main converter frame
        self.destroy()
        return Converter(root)


    def begin(self):
        # Checks if a difficulty was selected, if so moves on to practice frame
        if self.diff.get() != "None":
            self.destroy()
            return Practice(root, self.diff.get())
        else:
            self.error_label["text"] = "Please select a difficulty."
            

class Practice(Converter):
    # Frame where user answers practice questions
    # Child of converter class to use convert methods

    def __init__(self, master, diff):
        super(Practice, self).__init__(master)
        self.grid()
        self.widgets()
        self.diff = diff
        self.quiz()

        
    def widgets(self):
        # Title and Subtitle
        self.title = Label(self, text = "Convert", font = t_font)
        self.title.grid(row = 0, column = 1, columnspan = 3)
        self.subtitle = Label(self, text = "d - decimal : b - binary : h - hexadecimal")
        self.subtitle.grid(row = 1, column = 0, columnspan = 5)

        # Make question and entry boxes for 10 questions
        self.question_list = []
        self.entry_box_list = []
        self.answer_list = []
        for i in range(10):
            self.question_list.append(Label(self, pady = 4))
            self.question_list[i].grid(row = i + 2, column = 0, sticky = W)
            self.entry_box_list.append(Entry(self, width = 10))
            self.entry_box_list[i].grid(row = i + 2, column = 2, sticky = E)
       
        # Quit, Submit, and Cheat Sheet buttons
        self.quit_btn_frame = Frame(self, pady = 20, padx = 50)
        self.quit_btn_frame.grid(row = 12, column = 0, sticky = W)
        Button(self.quit_btn_frame, text = "Quit", command = self.menu).grid()

        self.submit_btn_frame = Frame(self, pady = 20, padx = 50)
        self.submit_btn_frame.grid(row = 12, column = 4, sticky = W)
        self.submit_btn = Button(self.submit_btn_frame, text = "Submit", command = self.submit)
        self.submit_btn.grid()
        
        self.cheat_btn_frame = Frame(self, padx = 0)
        self.cheat_btn_frame.grid(row = 2, column = 4, columnspan = 2, sticky = W)
        self.cheat_btn = Button(self.cheat_btn_frame, text = "Cheat Sheet", command = self.cheat)
        self.cheat_btn.grid()

        # Error label
        self.error_label = Label(self, font = 12)
        self.error_label.grid(row = 12, column = 0, columnspan = 5)
        
        
    def quiz(self):
        # Method to make 10 questions using the Question class and show them
        q_list = []
        for i in range(10):
            # While loop and q_list used to make sure there are no repeating questions
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
        # A cheat sheet to display the powers of 2, 10, and 16
        # If statement used to toggle button on and off
        if self.cheat_btn["relief"] == "raised":
        
            self.cheat_frame = Frame(self, bd = 2)
            self.cheat_frame.grid(row = 3,  column = 4, rowspan = 9, columnspan = 2, sticky = W)

            Label(self.cheat_frame, text = "Binary", font = u_font).grid(row = 0)
            
            # Make 6 labels to use for binary part of cheat sheet
            self.cheat_list_b = []
            for i in range(6):
                self.cheat_list_b.append(Label(self.cheat_frame))
                self.cheat_list_b[i].grid(row = i + 1, sticky = W)
                
            # Show powers of 2
            for i in range(5):
                self.cheat_list_b[i]["text"] = "2^" + str(i) + " = " + str(2 ** i) + "\t\t 2^"
                self.cheat_list_b[i]["text"] += str(i+5)+" = "+str(2 ** (i + 5)) 

            Label(self.cheat_frame, text = "Decimal\t\tHexadecimal", font = u_font).grid(row = 7)

            # Similar labels for decimal and hexidecimal
            self.cheat_list_dh = []
            for i in range(3):
                self.cheat_list_dh.append(Label(self.cheat_frame))
                self.cheat_list_dh[i].grid(row = i + 8, sticky = W)

            for i in range(3):
                self.cheat_list_dh[i]["text"] = "10^" + str(i) + " = " + str(10 ** i) 
                self.cheat_list_dh[i]["text"] += " \t16^"+str(i)+" = "+str(16 ** i) 
                
            # Make button sunken when presses
            self.cheat_btn["relief"] = "sunken"

        else:
            # If button is pressed when sunken, destroy the cheat sheet and raise the button
            self.cheat_btn["relief"] = "raised"
            self.cheat_frame.destroy()

    
    def menu(self):
        # Takes program back to main converter frame
        self.destroy()
        return Converter(root)


    def submit(self):
        # If submit button is pressed
        # Check that all questions are answered, or return an error prompt
        self.entry_list = []
        for i in range(10):
            if self.entry_box_list[i].get() == "":
                err = self.error_label["text"] = "Please answer all questions."
                return err
            else:
                self.entry_list.append(self.entry_box_list[i].get())
        
        # Condense all questions, answers, and entries to be passed on to the Practice Score frame
        self.q_and_a = []
        for i in range(10):
            q = self.question_list[i]["text"]
            e = self.entry_list[i]
            a = self.answer_list[i]
            self.q_and_a.append([q, e, a])

        # Destory practice frame and make practice score frame
        self.destroy()
        return Practice_Score(root, self.q_and_a)


class Practice_Score(Frame):
    # Shows the results of the practice quiz and gives a score

    def __init__(self, master, data):
        # Data input is the question, answer, and entry lists from practice class
        super(Practice_Score, self).__init__(master)
        self.grid()
        self.data = data
        self.widgets()
        self["borderwidth"] = 7

    def widgets(self):
        # Title and Subtitle
        self.title = Label(self, text = "Score", font = t_font)
        self.title.grid(row = 0, column = 0, columnspan = 5)
        self.subtitle = Label(self, font = ("Helvetica", 16))
        self.subtitle.grid(row = 1, column = 0, columnspan = 5)

        # Labels to display results
        Label(self, text = "Question", font = u_font).grid(row = 2, column = 0)
        Label(self, text = "Your Answer", font = u_font, padx = 20).grid(row = 2, column = 1)
        Label(self, text = "Corrext Answer", font = u_font, padx = 5).grid(row = 2, column = 2)
        Label(self, text = "Result", font = u_font, padx = 20).grid(row = 2, column = 3)
        
        # Make 10 rows of 4 labels to show each category
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

            # Check to see if the entries are same as the answers
            if self.data[i][1] == self.data[i][2]:
                self.result[i]["text"] = "Correct"
                self.score += 1
            else:
                self.result[i]["text"] = "Wrong"
        
        # Show Score
        self.subtitle["text"] = str(self.score) + "/10"
        
        # Quit and Try Again Buttons
        self.menu_btn_frame = Frame(self, pady = 15, padx = 20)
        self.menu_btn_frame.grid(row = 13, column = 0)
        Button(self.menu_btn_frame, text = "Quit", command = self.menu).grid()

        self.trya_btn_frame = Frame(self, pady = 15, padx = 20)
        self.trya_btn_frame.grid(row = 13, column = 3, sticky = E)
        Button(self.trya_btn_frame, text = "Try Again", command = self.trya).grid()
        
        # Message corresponding to the users results
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
 

    def menu(self):
        # Takes program back to main converter frame
        self.destroy()
        return Converter(root)


    def trya(self):
        # Takes program back to practice menu frame
        self.destroy()
        return Practice_Menu(root)


class Game_Menu(Frame):
    # Menu for game, similar to practice menu

    def __init__(self, master):
        super(Game_Menu, self).__init__(master)
        self.grid()
        self.widgets()
        self["borderwidth"] = 7


    def widgets(self):
        # Title
        Label(self, text = "Base Converter\nGame", font = t_font).grid(row = 0, column = 2)

        # labels for instructions
        self.inst_list = []
        for i in range(6):
            self.inst_list.append(Label(self))
            self.inst_list[i].grid(row = i + 1, column = 1, columnspan = 3, sticky =  W)
        
        self.inst_list[0]["text"] = "It is time to test your base conversion skills."
        self.inst_list[1]["text"] += "There are three difficulties you can select from."
        self.inst_list[2]["text"] += "You will be given 1 min to answer as many questions as you can"
        self.inst_list[3]["text"] += "Enter the correct answer in the associated textbox."
        self.inst_list[4]["text"] += "Click 'Skip' to skip question or 'Next' to continue" 
        self.inst_list[5]["text"] += "Click See Score when time expires."

        # Difficulty options, as radiobuttons
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
        
        # Back and Play Buttons
        self.back_btn_frame = Frame(self, pady = 20, padx = 20)
        self.back_btn_frame.grid(row = 8, column = 0, sticky = E)
        Button(self.back_btn_frame, text = "Back", command = self.back).grid()

        self.play_btn_frame = Frame(self, pady = 20)
        self.play_btn_frame.grid(row = 8, column = 4, sticky = E)
        Button(self.play_btn_frame, text = "Play", command = self.play).grid()
        
        # Error Label
        self.error_label = Label(self, font = 12)
        self.error_label.grid(row = 8, column = 2)
        

    def back(self):
        # Takes program back to main converter frame
        self.destroy()
        return Converter(root)

    def play(self):
        # Checks if a difficulty was selected, if so moves on to game frame
        if self.diff.get() != "None":
            self.destroy()
            return Game(root, self.diff.get())
        else:
            self.error_label["text"] = "Please select a difficulty."
    

class Timer(Frame):
    # Generates and displayes timer used in the game frame

    def __init__(self, master, remaining):
        super(Timer, self).__init__(master)
        self.remaining = remaining
        self["padx"] = 20
        
        # Make clock and message labels
        self.clock = Label(self, font = t_font)
        self.message = Label(self, font = ("Helvetica", 18))
        self.clock.grid(row = 0, sticky = W)
        self.message.grid(row = 1, sticky = W)


    def countdown(self):
        # Show clock counting down after every second

        # make minute and second calculations so clock can be shown in minutes 
        self.t_min = self.remaining // 60
        self.t_sec = self.remaining % 60
        if self.remaining > 0:
            if self.t_sec < 10:
                self.clock["text"] = str(self.t_min) + ":0" + str(self.t_sec) 
            else:
                self.clock["text"] = str(self.t_min) + ":" + str(self.t_sec) 

            self.remaining -= 1

            # Recursively run every second
            self.after(1000, self.countdown)

        # Change label texts and button states when time runs out
        else:
            self.clock["text"] = "0:00" 
            self.message["text"] = "Time is up!"
            self.master.skip_btn["state"] = "disabled"
            self.master.next_btn["state"] = "disabled"
            self.master.see_score_btn["state"] = "normal"


class Game(Converter):
    # Frame where game is played

    def __init__(self, master, diff):
        super(Game, self).__init__(master)
        self.diff = diff
        self.grid()
        self.widgets()
        

    def widgets(self):
        # Title and Subtitle
        self.title = Label(self, text = "Convert", font = t_font)
        self.title.grid(row = 0, column = 1, columnspan = 3)
        self.subtitle = Label(self, text = "d - decimal  :   b - binary  :   h - hexadecimal")
        self.subtitle["text"] += "\n\nCorrect: +20 pts   Wrong -10 pts   Skip -5 pts" 
        self.subtitle.grid(row = 1, column = 1, columnspan = 2, pady = 20)
        Label(self, text = "                   ", padx = 40).grid(row = 3, column = 0)

        # Create timer object for 1 minute countdown
        self.timer = Timer(self, 60)
        self.timer.grid(row = 3, column = 3, rowspan = 3, columnspan = 2, sticky = W)
       
        # Start button and question label
        self.start_frame = Frame(self, padx = 20, pady = 20)
        self.start_frame.grid(row = 4, column = 0)
        self.start_btn = Button(self.start_frame, text = "Start", command = self.start)
        self.start_btn.grid()
        
        self.question = Label(self)
        self.question.grid(row = 4, column = 0, columnspan = 3, sticky = W)
        
        # Skip and Next buttons
        self.skip_btn = Button(self, text = "Skip (-5 pts)", command = self.skip, state = "disabled")
        
        self.skip_btn.grid(row = 6, column = 1)
        self.next_btn = Button(self, text = "Next", command = self.next_q, state = "disabled")
        self.next_btn.grid(row = 6, column = 2, columnspan = 3, sticky = W)

        self.error_label = Label(self, font = 12)
        self.error_label.grid(row = 7, column = 1, columnspan = 4)

        # Quit and See Score button
        self.quit_frame = Frame(self, pady = 20)
        self.quit_frame.grid(row = 8, column = 0)
        Button(self.quit_frame, text = "Quit", command = self.menu).grid()

        self.see_score_btn = Button(self, text = "See Score", command = self.see_score)
        self.see_score_btn["state"] = "disabled"
        self.see_score_btn.grid(row = 8, column = 4, sticky = W)
        

    def load_question(self):
        # make a question object

        # While loop to prevent repetitive questions
        while True:
            obj = Question(root, self.diff)
            q = obj.question
            if q in self.q_list:
                continue
            else:
                # Show question and make entry frame
                self.question["text"] = str(self.i) + ".\t" +  q
                self.entry_frame = Frame(self, padx = 20)
                self.entry_frame.grid(row = 4, column = 1, sticky = E)
                self.entry = Entry(self.entry_frame, width = 12)
                self.entry.grid()

                # Append objects question and answer values to lists
                self.q_list.append(q)
                self.question_list.append(self.question["text"])
                self.answer_list.append(obj.answer)
                self.i += 1
                break
    

    def start(self):
        # When start button is pressed, lists are generated, timer starts countdown
        self.start_btn.destroy()
        self.skip_btn["state"] = "normal"
        self.next_btn["state"] = "normal"
        self.answer_list = []
        self.question_list = []
        self.entry_list = []
        self.q_list = []
        self.i = 1
        self.timer.countdown()
        self.load_question()
        

    def skip(self):
        # If skipped add None to entry and get new question
        self.entry_list.append(None)
        self.load_question()
        self.error_label["text"] = ""
           

    def next_q(self):
        # Check for entry and append it to list, if no entry show message
        if self.entry.get() == "":
            self.error_label["text"] = "Please enter answer or skip question"
        else:
            self.entry_list.append(self.entry.get())
            self.error_label["text"] = ""
            self.load_question()
            
           
    def see_score(self):
        # Delete last item off of answer and question lists because time ran out
        del self.question_list[-1]
        del self.answer_list[-1]

        # Condense data to be sent to game score frame
        self.q_and_a = []
        for i in range(len(self.entry_list)):
            self.q_and_a.append([self.question_list[i], self.entry_list[i], self.answer_list[i]])
        self.destroy()
        return Game_Score(root, self.q_and_a)
        

    def menu(self):
        # Takes program back to main converter frame
        self.destroy()
        return Converter(root)


class Game_Score(Frame):
    # Shows the results of the game and gives a score

    def __init__(self, master, data):
        super(Game_Score, self).__init__(master)
        self.grid()
        # Data is similar to practice score data but from game class
        self.data = data
        self.widgets()
        self["borderwidth"] = 7


    def widgets(self):
        # Title and Subtitle
        self.title = Label(self, text = "Score", font = t_font)
        self.title.grid(row = 0, column = 0, columnspan = 5)
        self.subtitle = Label(self, font = ("Helvetica", 16))
        self.subtitle.grid(row = 1, column = 0, columnspan = 5)

        # Labels to display results
        Label(self, text = "Question", font = u_font).grid(row = 2, column = 0)
        Label(self, text = "Your Answer", font = u_font, padx = 20).grid(row = 2, column = 1)
        Label(self, text = "Corrext Answer", font = u_font, padx = 5).grid(row = 2, column = 2)
        Label(self, text = "Result", font = u_font, padx = 20).grid(row = 2, column = 3)
        
        # 4 labels to show each category
        # Number of rows is equal to number of questions answered and skipped
        self.question = []
        self.yours = []
        self.correct = []
        self.result = []
        self.score = 0
        for i in range(len(self.data)):
            self.question.append(Label(self, text = self.data[i][0], padx = 4, pady = 3))
            self.question[i].grid(row = i + 3, column = 0, sticky = W)
            
            self.yours.append(Label(self, text = self.data[i][1]))
            self.yours[i].grid(row = i + 3, column = 1)
            
            self.correct.append(Label(self, text = self.data[i][2]))
            self.correct[i].grid(row = i + 3, column = 2)

            self.result.append(Label(self))
            self.result[i].grid(row = i + 3, column = 3)

            # Check if answers are correct and calculate score if correct, wrong, or skipped
            if self.data[i][1] == self.data[i][2]:
                self.result[i]["text"] = "Correct"
                self.score += 20
            elif self.data[i][1] == None:
                self.result[i]["text"] = "Skipped"
                self.score -= 5
            else:
                self.result[i]["text"] = "Wrong"
                self.score -= 10
                
        # Show score        
        self.subtitle["text"] = str(self.score)
    
        # Quit and Play Again Buttons
        self.menu_btn_frame = Frame(self, pady = 20, padx = 20)
        self.menu_btn_frame.grid(row = 13, column = 0)
        Button(self.menu_btn_frame, text = "Quit", command = self.menu).grid()

        self.playa_btn_frame = Frame(self, pady = 20, padx = 20)
        self.playa_btn_frame.grid(row = 13, column = 3, sticky = E)
        Button(self.playa_btn_frame, text = "Play Again", command = self.playa).grid()
           

    def menu(self):
        # Takes program back to main converter frame
        self.destroy()
        return Converter(root)

    def playa(self):
        # Takes program back to game menu frame
        self.destroy()
        return Game_Menu(root)



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

# Initialize converter frame
screen = Converter(root)
root.mainloop()

# Initial brainstorming thought process
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

for window setup i want to be able to find the display size and put my program in the middle of the screen
"""

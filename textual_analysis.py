# Kainoa Gaddis (c) 2014
# Create a textual analysis program with specific user requirements

# The requirements
"""
* Sentence length
* Word length
* Paragraph length
* Word use frequencies
* Unusual words

Extra
* Idiomatic usage
* Punctuation

"""

"""
Create a program that takes a user input to make a message.
  * Use user input over file so it is easier for people to copy paste stuff in rather\
 than having to change the txt file

set that message into a string

find the length of that sentence
  * Using the len function to find the number of characters
  * Find the number of word in that string
  * Find average sentence length if more than one sentence
  * Are people double spacing after a period

find average word length in the sentence
  * define a word as up to a " " - the space character
  * find the len of that word
  * could also find the average word length of the paragraph or entire message

find the paragraph length
  * use len function to find the character length
  * also find how many words in the paragraph
  * also find how many sentences in the paragraph
  * count \n to find number of paragraphs

word use
  * compare words to other words that have appeared in the sentence or paragraph.
    * add that word and the amount to a pool when counted multiple times. 
    * maybe use dictionary

unusual words
  * worry about later
  * Maybe compare to a list of most commonly used words
    * the common word list can be a text file

idioms
  * Worry about way later

punctuation
  * can be done early with the words
  * both recognize different punctuations and count how many times those punctuations were used
  * Possibly explore capitalization

Spell checker
  * build a spell checker to see if they speel words wrong
  * /usr/share/dict/words

find how many paragraphs or sentences in teh entire message

might want to use classes and objects to define sentences, words, and paragraphs



"""

"""
# Imports
from tkinter import *
import re

# Build GUI class
class GUI(Frame:
   
    def __init__(self, master):
        
        super(GUI, self).__init__(master)
        self.grid()
        self.widgets()

    def widgets(self):
        
        # Intro label
        self.intro = Label(self, text = "Enter Message:").grid(row = 0, column = 0, sticky = W)
        
        # Textbox
        self.text = Entry(self)
        self.text.grid(row = 0, column = 1, sticky = W)

        # Button
        self.button = Button(root, text = "Run Code", command = self.message)
        self.button.grid(row = 0, column = 2)

        # Results label
        self.results = Label(root, text = None)
        self.results.grid(row = 1, column = 0)
        
        # Results textbox
        

    def message(self):
        message = self.text.get()
        self.results["text"] = message
        return message

# Functions

# can be used for word length and sentence length
def average_length(lists):
    

    # Find the average word length of the sentence
    length_list = []
    for thing in lists:
        length = len(thing)
        length_list.append(length)

    list_sum = 0
    for i in length_list:
        list_sum += i

    # Be careful about the length of the floats
    list_avg = list_sum / len(length_list)

    print("%.2f" % list_avg)


def length(lists):
    
    length = len(lists)
    return length


def split_up(special, string):
    lists = re.split(special, string)
    if "" in lists:
        lists.remove("")
    return lists


# The Main loop
root = Tk()
root.title("Textual Analysis")
root.geometry("500x250+800+300")

app = GUI(root)

# The message
message = app.message()

# might have to split sentence into pieces
word_list = split_up("\W+", message)

# Split message into sentences
sentence_list = split_up("[.!?]", message)

words_in_sentence = []
for sentence in sentence_list:
    sent_words = split_up("\W+", sentence)
    words_in_sentence.append(sent_words)


root.mainloop()


# Tests
print(message)
print ()
print(word_list)
print()
print(sentence_list)
print()
print(words_in_sentence)

# Print functions
print("\nYour message is", length(sentence_list), "sentences long.")
print("\nYour message is", length(word_list), "words long.")
print()
# Average characters in a word of the whole message
print("The average number of letters in a word: ", end="")
average_length(word_list)
print()
# Average characters in a sentence
print("The average number of characters in a sentence: ", end="")
average_length(sentence_list) 
print()
# Average words in a sentence for the whole message
print("The average number of words in a sentence: ", end="")
average_length(words_in_sentence)
print()
"""
#########################################################################################

# Imports
from tkinter import *
import re



# Functions

# can be used for word length and sentence length
def average_length(lists):
    """ Find the average word length of a sentence """

    # Find the average word length of the sentence
    length_list = []
    for thing in lists:
        length = len(thing)
        length_list.append(length)

    list_sum = 0
    for i in length_list:
        list_sum += i

    # Be careful about the length of the floats
    list_avg = list_sum / len(length_list)

    return list_avg


def length(lists):
    """ Finds length of a list """
    length = len(lists)
    return length


def split_up(special, string):
    lists = re.split(special, string)
    if "" in lists:
        lists.remove("")
    return lists

def the_message():
    message = text_box.get(0.0, END)
    text_label["text"] += message
    text_box.delete(0.0, END)

    # might have to split sentence into pieces
    word_list = split_up("\W+", message)

    # Split message into sentences
    sentence_list = split_up("[.!?]", message)

    words_in_sentence = []
    for sentence in sentence_list:
        sent_words = split_up("\W+", sentence)
        words_in_sentence.append(sent_words)
    

    sent["text"] += str(length(sentence_list))
    words["text"] += str(length(word_list))
    avg_word_length["text"] += "%.2f" % average_length(word_list)
    avg_sent_length["text"] += "%.2f" % average_length(sentence_list)
    avg_word_per_sent["text"] += "%.2f" % average_length(words_in_sentence)


    #Tests
    print(message)
    print ()
    print(word_list)
    print()
    print(sentence_list)
    print()
    print(words_in_sentence)
    

    # Print functions
    print("\nYour message is", length(sentence_list), "sentences long.")
    print("\nYour message is", length(word_list), "words long.")
    print()
    # Average characters in a word of the whole message
    print("The average number of letters in a word: ", end="")
    print(average_length(word_list))
    print()
    # Average characters in a sentence
    print("The average number of characters in a sentence: ", end="")
    print(average_length(sentence_list)) 
    print()
    # Average words in a sentence for the whole message
    print("The average number of words in a sentence: ", end="")
    print(average_length(words_in_sentence))
    print()

    return message


# The Main loop
root = Tk()
root.title("Textual Analysis")
root.geometry("500x250+800+300")

# Intro label
intro = Label(root, text = "Enter Text:").grid(row = 0, column = 0, sticky = W)
        
# Textbox
text_box = Text(root, width = 25, height = 5, wrap = WORD)
text_box.grid(row = 0, column = 1, sticky = W)

# Results labels
text_label = Label(root, text = "The Text: ")
text_label.grid(row = 1, column = 0, columnspan = 5, sticky = W)

sent = Label(root, text = "Number of sentences: ")
sent.grid(row = 2, column = 0, columnspan = 2, sticky = W)

words = Label(root, text = "Number of words: ")
words.grid(row = 3, column = 0, sticky = W) 

avg_word_length = Label(root, text = "Avg. word length: ")
avg_word_length.grid(row = 4, column = 0, sticky = W)

avg_sent_length = Label(root, text = "Avg. sentence length: ")
avg_sent_length.grid(row = 5, column = 0, columnspan = 2, sticky = W)

avg_word_per_sent = Label(root, text = "Avg. words per sentence: ")
avg_word_per_sent.grid(row = 6, column = 0, columnspan = 2, sticky = W)

# Button
button = Button(root, text = "Run Code", command = the_message)
button.grid(row = 0, column = 2)

# Results textbox





root.mainloop()

"""
What to work on

remove any empty words or sentences

work on identifying paragraphs

rounding floating number issues

identifying most common words

identifying strange words

restart button to do again

clear button

how to compare multiple things of text

what to do if input text has a number with decimal point in it
"""

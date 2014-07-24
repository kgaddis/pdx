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
# Imports
from tkinter import *
import re

# can be used for word length and sentence length
def average_length(list):
    """ Find the average word length of a sentence """

    # Find the average word length of the sentence
    length_list = []
    for thing in list:
        length = len(thing)
        length_list.append(length)

    list_sum = 0
    for i in length_list:
        list_sum += i

    # Be careful about the length of the floats
    list_avg = list_sum / len(length_list)

    print(list_avg)


def message_length(message):
    """ Finds length of message """
    message_length = len(message)
    
    return message_length


def number_of_words(word_list):
    """ Find number of words in a message """
    number_of_words = len(word_list)
    print(number_of_words)


# The Main loop

# The message
message = "Hi, my name is Kainoa. This is the second sentence! This last sentence completes the paragraph.\n This is a new paragraph."

# might have to split sentence into pieces
word_list = re.split("\W+", message)

# Split message into sentences
sentence_list = re.split('[.!?]', message)


message_length(message)
number_of_words(word_list)


print("\nYour message is", message_length(word_list), "words long.")
print("\nYour message is", message_length(sentence_list), "sentences long.")
print()
print(word_list)
print()
print(sentence_list)
print()
# Average characters in a word of the whole message
print("The average number of characters in a word: ", end="")
average_length(word_list)
print()
# Average characters in a sentence
print("The average number of characters in a sentence: ", end="")
average_length(sentence_list) 
print()
# Average words in a sentence for the whole message
print("The average number of words in a sentence: ", end="")

print()



"""
# Build GUI
root = Tk()
root.title("Textual Analysis")
root.geometry("500x250+800+300")

intro = Label(root, text = "Enter Message:").grid(row = 0, column = 0, sticky = W)
text = Text(root, width = 35, height = 5, wrap = WORD)
text.grid(row = 0, column = 1, rowspan = 2, sticky = W)
button = Button(root, text = "Run Code", command = number_of_words(word_list))
button.grid(row = 0, column = 2)
results = Label(root, text = number_of_words(word_list)) # Broken label and button
results.grid(row = 1, column = 2)


root.mainloop()
"""

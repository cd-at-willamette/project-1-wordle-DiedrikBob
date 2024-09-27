########################################
# Name: Diedrik
# Collaborators (if any): - 
# GenAI Transcript (if any): - 
# Estimated time spent (hr): a lot
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

row = 0


def wordle():
    
    def get_word_from_row(row):
        word_from_row = ""
        for i in range(5):
            word_from_row += gw.get_square_letter(row, i)
        #gw.show_message(word_from_row)
        word_from_row = word_from_row.lower()
        return word_from_row


    def random_five_letter_word():
        random.shuffle(ENGLISH_WORDS)
        for word in ENGLISH_WORDS:
            if len(word) == 5:
                str_word = word.lower()
                return str_word


    def word_to_row(word:str, row:int):
        for i in range(5):    
            gw.set_square_letter(row, i, word[i])


    def compare_word():
        for index in range(len(wordle_word)):
            #for letter in range(len(get_word_from_row(row))):
            #if c in wordle_word:

            if get_word_from_row(row)[index] in wordle_word:
                gw.set_square_color(row, index, "yellow") 

            if get_word_from_row(row)[index] == wordle_word[index]:
                gw.set_square_color(row, index, "green")

            else:
                gw.set_square_color(row, index, "grey")


    def check_affiration(row):

        if get_word_from_row(row) in ENGLISH_WORDS:
            gw.show_message("Yes, its a word.")
        else:
            gw.show_message("It's not a word.")


    def change_row():
        gw.set_current_row(row + 1)
        

    def enter_action():
            check_affiration(row)
            compare_word()
            change_row()
            print(get_word_from_row(row))
            return row + 1

#########################
# calling up functions
#########################
  

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    #gw.add_enter_listener(compare_word)

    

    #word_to_row("Hello",0)

    #guess_word = get_word_from_row()

    wordle_word = random_five_letter_word()

    print(wordle_word)
    

# Startup boilerplate
if __name__ == "__main__":
    wordle()


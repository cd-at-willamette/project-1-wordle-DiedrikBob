########################################
# Name: Diedrik Boberg
# Collaborators (if any): -
# GenAI Transcript (if any): -
# Estimated time spent (hr): 13
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    def get_word_from_row():
        row = gw.get_current_row() # getting current row
        word_from_row = "" # creates empty word
        for i in range(5):
            word_from_row += gw.get_square_letter(row, i) # adding letter for letter to our "" - word

        word_from_row = word_from_row.lower() # sets everything to lowercase letters
        return word_from_row # returns the word from row



    def contains_repeated_letters(word):
        for index in range(len(word)): #loop through every letter of word
            for letter in range(index + 1, len(word)):
                if word[index] == word[letter]: #if letter is equal then the letter is repeating
                    return True
        else: 
            return False



    def random_five_letter_word():
        random.shuffle(ENGLISH_WORDS)
        for word in ENGLISH_WORDS: # goes through every word in ENGLISH_WORDS 
            if len(word) == 5: # until we reach a word with length of 5
                if contains_repeated_letters(word) == False: # if the word doesn't contain a repeated letter we assign that word to our wordle_word
                    str_word = word.lower()
                    return str_word



    def compare_word():
        row = gw.get_current_row() 
        my_word = get_word_from_row()

        for index in range(len(wordle_word)):
            if my_word[index] in wordle_word and my_word[index] == wordle_word[index]: # if the letter is in the wordle_word and in the same place as the correct letter then we color the square green
                gw.set_square_color(row, index, "green") 
                my_word = my_word.replace(my_word[index], "-") # we replace that letter with "-" to make sure that we already colored that square
                #print(my_word, index) # test to see what "my_word" looks like after replacing the letter

        for index in range(len(wordle_word)): # doing another for loop because we need to see if there are any letters that aren't green, but in the wrong place
            if gw.get_square_color(row,index) !=  "green": 
                if my_word[index] in wordle_word and my_word[index] != wordle_word[index]:
                        gw.set_square_color(row, index, PRESENT_COLOR)
                        my_word = my_word.replace(my_word[index], "-") # replacing that letter with "-" to make sure that we already colored that square
                        #print(my_word, index) # test to see what "my_word" looks like after replacing the letter
                else:
                    gw.set_square_color(row, index, "grey")

    

    def check_green_letters():
        greens = 0
        for i in range(len(wordle_word)): # we go through the word
            if get_word_from_row()[i] == wordle_word[i]: # for each letter we compare it to the wordle word
                greens += 1 # when the letter is in the correct place we add one to "greens"
        return greens



    def check_win():
        if check_green_letters() == 5: # if we get 5 greens we win
            gw.show_message("You're Awesome! Well done!")
            return True
        else:
            return False



    def check_affiration():
        if get_word_from_row() in ENGLISH_WORDS and len(get_word_from_row()) == 5: # checking if word is an english word and is 5 letters long
            return True
        else:
            gw.show_message("It's not a word.")
            return False



    def change_row():
        row = gw.get_current_row() # getting current row
        if gw.get_current_row() != 5 and check_win() == False: # if we haven't won yet or the current row is unequal to five we move on one row
                gw.set_current_row(row + 1)
        elif gw.get_current_row() == 5 and check_win() == False: # if we reached the bottom we loose if we didn't manage to get 5 greens
            gw.show_message("Sorry, the word was:" + " "+ wordle_word.upper()) # letting the player know what the word was
 


    def color_keys():
        for i in range(len(wordle_word)):
            if get_word_from_row()[i] == wordle_word[i]: # if letter is in word and at correct place we color it green
                gw.get_key_color(get_word_from_row()[i])
                gw.set_key_color(get_word_from_row()[i], "green")
            elif get_word_from_row()[i] in wordle_word: # if letter in word and and the key is not already green we color it yellow/PRESENT_COLOR
                if gw.get_key_color(get_word_from_row()[i]) != "green":
                    gw.set_key_color(get_word_from_row()[i], PRESENT_COLOR)
            else: # else we color it grey
                gw.get_key_color(get_word_from_row()[i])
                gw.set_key_color(get_word_from_row()[i], "grey")



    def enter_action():
        if check_affiration() == True: #first we check if word is even an english word before we move on
            compare_word() # comparing word and color the letters 
            color_keys() # coloring the keys
            change_row() # changing row
        
#########################
# calling up functions
#########################

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    wordle_word = random_five_letter_word()

# Startup boilerplate
if __name__ == "__main__":
    wordle()

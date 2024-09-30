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


def wordle():
    
    def get_word_from_row():
        row = gw.get_current_row()
        word_from_row = ""
        for i in range(5):
            word_from_row += gw.get_square_letter(row, i)

        word_from_row = word_from_row.lower()
        return word_from_row



    def contains_repeated_letters(word):
        for index in range(len(word)): #loop through every letter of word
            for letter in range(index + 1, len(word)):
                if word[index] == word[letter]: #if letter is equal then the letter is repeating
                    return True
                
        else: 
            return False



    def random_five_letter_word():
        random.shuffle(ENGLISH_WORDS)
        for word in ENGLISH_WORDS:
            if len(word) == 5: #and 
                if contains_repeated_letters(word) == False:
                    str_word = word.lower()
                    return str_word



    def compare_word():
        row = gw.get_current_row()
        my_word = get_word_from_row()

        for index in range(len(wordle_word)):
            
            if my_word[index] in wordle_word and my_word[index] == wordle_word[index]:
                gw.set_square_color(row, index, "green")
                my_word = my_word.replace(my_word[index], "-")
                print(my_word, index)
        for index in range(len(wordle_word)):
            if gw.get_square_color(row,index) !=  "green":
                if my_word[index] in wordle_word and my_word[index] != wordle_word[index]:
                        gw.set_square_color(row, index, PRESENT_COLOR)
                        my_word = my_word.replace(my_word[index], "-")
                        print(my_word, index)
                else:
                    gw.set_square_color(row, index, "black")

    
    def check_green_letters():
        greens = 0
        for i in range(len(wordle_word)):
            if get_word_from_row()[i] == wordle_word[i]:
                greens += 1
            
        return greens

    def check_win():
        if check_green_letters() == 5:
            gw.show_message("You're Awesome! Well done!")
            return True
        else:
            return False

    def check_affiration():
        if get_word_from_row() in ENGLISH_WORDS and len(get_word_from_row()) == 5:
            return True
        
        else:
            gw.show_message("It's not a word.")
            return False

    def change_row():
        row = gw.get_current_row()
        if gw.get_current_row() != 5 and check_win() == False:
                gw.set_current_row(row + 1)
            
        elif gw.get_current_row() == 5 and check_win() == False:
            gw.show_message("""Sry buddy, the game is over. But YOU'RE AWESOME!""") # Try again. Never give up! You can make this!""")
            
    
    def color_keys():
        for i in range(len(wordle_word)):
            if get_word_from_row()[i] == wordle_word[i]:
                gw.get_key_color(get_word_from_row()[i])
                gw.set_key_color(get_word_from_row()[i], "green")

            elif get_word_from_row()[i] in wordle_word:
                if gw.get_key_color(get_word_from_row()[i]) != "green":
                    gw.set_key_color(get_word_from_row()[i], PRESENT_COLOR)
            
            else:
                gw.get_key_color(get_word_from_row()[i])
                gw.set_key_color(get_word_from_row()[i], "black")

            #gw.set_current_row()

    

    def enter_action():
        
        if check_affiration() == True:
            compare_word()
            check_win()
            color_keys()
            change_row()
        
            

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
    
    word_list = []
    for i in range(len(wordle_word)):
        word_list.append(wordle_word[i])
        
    print(word_list)

# Startup boilerplate
if __name__ == "__main__":
    wordle()


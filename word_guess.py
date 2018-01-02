# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:00:50 2016

@author: marco
"""

import random
import string

def choose_word(word):
    '''
    chooses a random word from the list
    '''
    word_to_guess = random.choice(word)
    return word_to_guess
    
def available_letters():
    '''
    displays the available letters
    '''
    available = string.ascii_lowercase
    print("Available letters: %s" %(available))
    
def visible_letters(word_to_guess, guesses, letters):
    '''
    Displays visible letters and dashes
    '''
    #Chooses a random word and assigns the amount of guesses
    word = word_to_guess
    letters = ''
    
    #loops through the word to create dashes and input the letters
    while guesses > 0:        
        dashes = 0
        for char in word:      
            if char in letters:    
                print(char , end="")
            else:
                print( "_ ", end="")     
                dashes += 1    
        if dashes == 0:  
            print("")
            print("You won")  
            break              
        
def prompt_for_guess(guesses, letters):
    '''
    Asks the user for a guess
    '''
    #Displays amount of letters available, prompts for a guess, displays guesses remaining, and combines the letters
    print("\n\n")
    available_letters()
    print("%d incorrect guesses remaining" %(guesses))
    guess = input("Please enter the letter you wish to guess: ")
    letters += guess
    return letters, guess
    
def validates_letter(guess, word, guesses):
    #checks to see if the guess is in the word                    
    if guess in word:
        print("Good Job! The letter %s is in the word!" %(guess))
        print("\n")
        
    #checks to see if the guess is in the word
    if guess not in word:  
        guesses -= 1        
        print("The letter %s is not in the word." %(guess))  
        print("\n")
        if guesses == 0:           
            print("You Loose")
    
def main():
    #opens file
    infile = open("states.txt", "r")
    
    #makes words into a list
    word = infile.read().split()
    #print(word)
    
    #calls the function and displays letter count
    word_to_guess = choose_word(word)
    print("The word to guess has %d letters \n" %(len(word_to_guess)))
    
    guesses = 7
    letters = ''
    
    while guesses > 0:
        visible_letters(word_to_guess, guesses, letters)
        (letters, guess) = prompt_for_guess(guesses, letters)
        validates_letter(guess, word, guesses)
                
    #closes the file
    infile.close()
    
main()
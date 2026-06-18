import random
print("Welcome to Hangman game!")
lst=["Apple", "Banana", "Grapes", "Mango", "Orange"]
#stores a random word from the list
word=random.choice(lst)
#guessed letters
guessed_letters=[]
#number of attempts 
attempts=6
while attempts>0:
    #display the word with guessed letters and underscores for unguessed letters
    display_word=""
    for letter in word:
        if letter.upper() in guessed_letters:
            display_word+=letter+" "
        else:
            display_word+="_ "
    print(display_word)
    
   
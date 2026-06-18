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

     #check if the player has guessed the whole word
    if "_" not in display_word:
        print("Congratulations! You've guessed the word:", word)
        break
    
    #getting player's guess
    guess=input("Guess a letter: ").upper()
    
    #checking if the guess is valid
    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    #checking if the letter is already guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    
    #add the guessed letter to the list
    guessed_letters.append(guess)
    
   
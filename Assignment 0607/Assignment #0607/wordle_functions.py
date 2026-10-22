import random

#Choose a random 5 letter word
def choose_word():
    words = ["APPLE", "WHICH", "THEIR", "SLICE", "PLANT", "CHAIR","DRUGS","TRUCK","POKER","MONEY"]
    word = list(random.choice(words))
    return word

#Get and store guesses from user
def get_guess(previous_guesses):
    while True:
        guess = input("Guess a 5 letter word: ").upper()

        if len(guess) != 5:
            print("Your guess must be exactly 5 letters.")

        elif not guess.isalpha():
            print("Please enter letters only.")

        elif list(guess) in previous_guesses:
            print("You already guessed that word.")

        else:
            guess = list(guess)
            return guess

#Evaluate if letter is in the word or not
def evaluate_guess(guess,word):
    feedback = ""

    for i in range(5):
        if guess[i] == word[i]:
            feedback += "G"
        elif guess[i] in word:
            feedback += "Y"
        else:
            feedback += "-"
    return feedback

#Display guess and feedback
def display_guess(guess, feedback):
    print("Guess:   "," ".join(guess))
    print("Feedback:", " ".join(feedback))

#If user guessed random word correctly
def has_won(guess, word):
    return guess == word
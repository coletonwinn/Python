from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

play_again = "yes"

while play_again == "yes":

#Declare variables
    word = choose_word()
    previous_guesses = []
    won = False

#Welcome user and explain rules
    print("Welcome to Mystery Wordle!")
    print("Guess the five-letter word.")
    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter is not in the word")
    print("")

#Loop guesses and evaluation
    for attempt in range(1, 7):
        print("Attempt", attempt, "of 6")
        guess = get_guess(previous_guesses)

        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, word)
        display_guess(guess, feedback)
        print("")

#Game end
        if has_won(guess, word):
            print("Congratulations! You solved the puzzle.")
            won = True
            break

    if not won:
        print("That was all 6 attempts!")
        print("The word was", "".join(word))

    play_again = input("Would you like to play again? (yes or no) ").lower()

print("Thanks for playing!")
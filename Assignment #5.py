#Create Variables
import random

player_wins = 0
computer_wins = 0
games_played = 0

#Custom Functions
def get_player_choice ():
    player_choice = str(input("Enter rock, paper, or scissors: "))
    while player_choice.lower() not in ["rock", "paper", "scissors"]:
        print("Invalid response. Try again")
        player_choice = str(input("Enter rock, paper, or scissors: "))
    return player_choice.lower()

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "Win"
    elif player_choice == "rock" and computer_choice == "paper":
        return "Loss"
    elif player_choice == "paper" and computer_choice == "scissors":
        return "Loss"
    elif player_choice == "paper" and computer_choice == "rock":
        return "Win"
    elif player_choice == "scissors" and computer_choice == "rock":
        return "Loss"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "Win"

#Opening statement and questions
print("Welcome to ROCK, PAPER, SCISSORS!!")
num_rounds = int(input("How many rounds would you like to play? "))
while num_rounds % 2 != 1:
    print("Invalid number of rounds. Please pick an odd number")
    num_rounds = int(input("How many rounds would you like to play? "))

#Play the rounds + Count rounds
while games_played != num_rounds:
    player_choice = get_player_choice()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("--------------")
    print(f"THE COMPUTER CHOSE: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    if result == "Win":
        print("YOU WIN")
        print("--------------")
        player_wins += 1
        games_played += 1
    elif result == "Loss":
        print("YOU LOSE")
        print("--------------")
        computer_wins += 1
        games_played += 1
    else:
        print("TIE, REDO")

    
#Summary
print("GAME SUMMARY")
print("--------------")
print(f"ROUNDS PLAYED: {games_played}")
print(f"COMPUTER WINS: {computer_wins}")
print(f"YOUR WINS: {player_wins}")
print("--------------")
if computer_wins > player_wins:
    print("YOU LOSE")
elif computer_wins == player_wins:
    print("TIE GAME")
else:
    print("YOU WIN")
print("THANKS FOR PLAYING")
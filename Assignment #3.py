repeat = "y"

#Prompt
while repeat.lower() == "y":
    print("Hey! Lets play a game!")
    response = int(input("Pick a number 1-100: "))
    while (response < 0 or response > 100):
        print("Invalid Response")
        response = int(input("Pick a number 1-100: "))

    #Generate random integer
    import random
    random_number = random.randint(1,100)

    #attempt counter
    attempts = 1


    #Higher or lower
    while response != random_number:
        if (response < 0 or response > 100):
            print("Invalid Response")
            response = int(input("Pick a number 1-100: "))
        elif response > random_number:
            print("Lower")
            attempts = attempts + 1
            response = int(input("Pick a number 1-100: "))
        elif response < random_number:
            print("Higher")
            attempts = attempts + 1
            response = int(input("Pick a number 1-100: "))


    #Final Message
    print("")
    print("You got it right!")
    print (f"It took you {attempts} tries!")
    print("")
    if attempts >= 10:
        print("You need to lock in...")
    elif attempts == 8 or attempts == 9:
        print("Took a little longer, but you got there...")
    elif attempts == 6 or attempts == 7:
        print("Good Job!")
    elif attempts == 5 or attempts == 4:
        print("Impressive!")
    elif attempts >= 3:
        print("Amazing!")

    #Play Again?
    repeat = str(input("Enter y to play again: "))

print("")
print("Alright! Thanks for playing!")

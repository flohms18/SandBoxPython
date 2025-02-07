import random


def PriceisRight():
    Number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    Guess = int(input())
    Attempts = 0
    while Guess != Number and Attempts < 10:
        

        if Guess < Number:  
            print("Sorry, you guessed too low. Try again.")
            Attempts += 1
            print("It took you", Attempts, "attempts.")

            Guess = int(input())

        elif Guess > Number:
            print("Sorry, you guessed too high. Try again.")
            Attempts += 1
            print("It took you", Attempts, "attempts.")
            Guess = int(input())
    if Guess == Number:
        print("Congratulations! You guessed the correct number in", Attempts, "attempts.")




PriceisRight()
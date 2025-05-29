# """
# Task:
# Create guessing game so that the user only has 3 chances to guess the number. After 3 failed attempts, the game should end and reveal the correct number.
import random

def play():
    secret = random.randint(1,10)
    count = 0

    while True:
        try:
            guess = int(input("Enter a number between 1 and 10"))
        except ValueError:
            print("Please enter a valid value")
            continue

        count+=1

        if count == 3 and secret != guess:
            print("You have failed the game")
            print(f"The correct answer was {secret}")
            break
        elif count == 2 and secret != guess:
            print("You have one attempt left")

        match guess:
            case _ if secret == guess:
                print("you guessed correct")
                break
            case _ if guess < secret:
                print("You guessed wrong pick a bigger number")
            case _ if guess >secret:
                print("you guessed wrong pick a smaller number")
while True:
    play()
    question = str(input("Do you want to play again? yes/no "))
    if question != "yes":
        print("Thanks for playing")
        break
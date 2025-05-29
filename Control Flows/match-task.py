import random
# def play_game():
#     secret_number = random.randint(1,10)
#     guess = int(input("Enter a number between 1 and 10: "))
    

#     match guess:
#         case _ if guess == secret_number:
#             print("You guessed correct")
#         case _ if guess > secret_number:
#             print("You guessed wrong, try a smaller number")

#         case _ if guess < secret_number:
#             print("You guessed wrong,try a bigger number")

# while True:
#     play_game()
#     counter=0
#     again = input("Do you want to play again? (yes/no): ").lower()
#     counter+=1
#     print(f"You have guessed {counter} times")
#     if again != 'yes':
#         print("Thanks for playing! Goodbye.")
#         break


def play_game():
    secret = random.randint(1,10)
    count = 0

    while True:
        try:
            guess = int(input("guess a number between 1 and 10: "))
        except ValueError:
            print("Sorry, Enter a number between 1-10")

        count +=1

        if count == 3 and secret != guess:
            break
        elif count ==2 and secret!=guess:
            print("You have only one attempt left")

        match guess:
            case _ if guess == secret:
                print("You guessed correct")
                break
            case _ if guess > secret:
                print("you guessed incorrect, pick a smaller number")
            case _ if guess < secret:
                print("You guessed incorrectly pick a bigger number") 
        
                  
while True:
    play_game()
    question = str(input("Do you wish to play again? yes/no ")).lower()
    if question != "yes":
        print("Have a lovely day")
        break




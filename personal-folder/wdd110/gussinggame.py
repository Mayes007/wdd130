#Python

import random

number_to_guess=random.randint(1,100)

print(number_to_guess)

guess=-1

while guess != number_to_guess:
    guess=int(input("What is your guess "))

    if guess < number_to_guess:
        print ("Higher")
    elif guess > number_to_guess:
        print ("Lower")
    else:
        print ("You guessed it!")

        keep_playing="yes"

        while keep_playing=="yes":
            number_to_guess=random.randint(1,1000)

            guess_count=0

            guess=-1

            while guess!=number_to_guess:
                guess=int(input("What is your guess? "))
                guess_count=guess_count +1

                if guess<number_to_guess:
                    print("Higher")

                elif guess > number_to_guess:
                    print("Lower")

                else:
                    print("You guessed it!")

                    print(f"It took you {guess_count} guesses")
                   
                    keep_playing=input("Would you like to play again (yes/no)? ")
                    
                    print("Thank you for playing. Goodbye.")



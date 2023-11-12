#Python

import random

secret_word=["mosiah", "helaman", "moroni", "nephi", "alma"]
secret_word=random.choice(secret_word)

guesses=0
correct=False

print("Welcome to the word guessing game!")

while not correct:
    user_guess=input("What is your guess? ").lower()
    guesses+=1
    if user_guess==secret_word:
        correct=True
        print("Congratulations! You guessed it!")
        print(f"It took you {guesses} guess{'es' if guesses > 1 else ''}.")

    else:
        print("Your guess was not correct.")

        hint="_"*(secret_word)
        while not correct:
            print(f'Your hint is: {hint}')
            user_guess=input("What is your guess? ").lower
            guesses +=1

            if user_guess== secret_word:
                correct=True
                break
            if len(user_guess) !=len(secret_word):
                print('Sorry, the guess must have the same number of letters as the secret word.')
                continue

            hint=''
            for s, g in zip(secret_word, user_guess):
                if s==g:
                    hint+=s.upper()
                elif g in secret_word:
                    hint+=g.lower()
                else:
                    hint+='_'

    print(f"Congratulations! You guessed it!\nIt took you {guesses} guess{'es' if guesses > 1 else ''}.")
 



        
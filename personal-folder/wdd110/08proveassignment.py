import random

secret_words = ["mosiah", "helaman", "moroni", "nephi", "alma"]
secret_word = random.choice(secret_words)

guesses = 0
correct = False

print("Welcome to the word guessing game!")

while not correct:
    user_guess = input("What is your guess? ").lower()
    guesses += 1

    if user_guess == secret_word:
        correct = True
        break

    if len(user_guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    # Generate the hint based on the rules
    hint = ""
    for i, (s, g) in enumerate(zip(secret_word, user_guess)):
        if s == g:
            hint += g.upper()
        elif g in secret_word and g != s:
            hint += g.lower()
        else:
            hint += "_"

    print(f"Your hint is: {hint}")

print(f"Congratulations! You guessed it!\nIt took you {guesses} guess{'es' if guesses > 1 else ''}.")

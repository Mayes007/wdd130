import random

# Define a list of secret words
secret_words = ["mosiah", "helaman", "alma", "moroni", "nephi"]

# Choose a random secret word from the list
secret_word = random.choice(secret_words)

# Initialize variables
guesses = 0
correct = False

# Welcome message
print("Welcome to the word guessing game!")

# Loop until the user guesses the word correctly
while not correct:
    # Display initial hint with underscores
    hint = ["_"] * len(secret_word)
    print("Your hint is:", " ".join(hint))
    
    # Prompt the user for a guess
    user_guess = input("What is your guess? ").lower()
    
    # Check if the guess has the same length as the secret word
    if len(user_guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        guesses += 1
        correct = True

        # Check the guess against the secret word and generate the hint
        for i in range(len(secret_word)):
            if user_guess[i] == secret_word[i]:
                hint[i] = user_guess[i].upper()
            elif user_guess[i] in secret_word:
                hint[i] = user_guess[i]
            else:
                hint[i] = "_"

        # Display the updated hint
        print("Your hint is:", " ".join(hint))

# Display the number of guesses it took to guess the word
print(f"Congratulations! You guessed it!\nIt took you {guesses} guess{'es' if guesses > 1 else ''}.")

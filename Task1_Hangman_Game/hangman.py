import random

words = ["apple", "mango", "grapes", "orange", "banana"]
word = random.choice(words)

guessed = []
attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in word:
        guessed.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Game Over! The word was:", word)
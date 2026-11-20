import random

name = input("What is your name?")
print("Good luck!", name)

words = ["computer", "laptop", "window", "desktop"]
word = random.choice(words)

guessed = []
attempts = 6

print("Guess the character!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed.append(guess)
        print("Correct guess!")
    else:
        guessed.append(guess)
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("You lost! The word was:", word)

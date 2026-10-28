import random

words = ["apple", "mango", "tiger", "chair", "house"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_guesses:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses left:", max_guesses - wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The word was:", word)
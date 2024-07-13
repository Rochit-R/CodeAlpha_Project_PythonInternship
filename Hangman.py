import random

select = ['algorithm', 'neural', 'network', 'machine', 'learning', 'data', 'intelligence', 'supervised']

def choose_word():

    return random.choice(select)

def get_hint(word, guessed_letters):

    hint = []
    for letter in word:
        if letter in guessed_letters:
            hint.append(letter)
        else:
            hint.append('_')
    return ' '.join(hint)

def hangman():

    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6
    print("Welcome to Hangman! , Guess AI-related words.")

    while incorrect_guesses < max_attempts:

        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"Word: {display_word}")
        if '_' not in display_word:

            print("Congratulations! You guessed the word.")
            break

        guess = input("Guess a letter or type 'hint' for a hint: ").lower()

        if guess == 'hint':

            print(f"Hint: {get_hint(word, guessed_letters)}")
            continue

        if len(guess) != 1 or not guess.isalpha():

            print("Please enter a single letter or 'hint'.")
            continue

        if guess in guessed_letters:

            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:

            print("Correct!")

        else:

            print("Incorrect guess.")
            incorrect_guesses += 1

        print(f"Attempts remaining: {max_attempts - incorrect_guesses}")

    if '_' in display_word:

        print(f"Sorry, you ran out of attempts. The word was '{word}'.")

hangman()

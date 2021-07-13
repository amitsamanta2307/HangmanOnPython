import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    word_list = ["abruptly", "buzzwords", "jaundice"]
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    # Create blanks
    display = []
    for _ in range(word_length):
        display.append("_")

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            print(f"{guess} is not in the word")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

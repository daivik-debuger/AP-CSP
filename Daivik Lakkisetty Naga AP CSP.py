# Name: Daivik Lakkisetty Naga
# Program Name: Crack the Code
# Program Date: October 19, 2026
# Program Summary: Guess a random secret code before running out of tries.

import random
from itertools import count

# These are the settings from the assignment.
code_length = 4
smallest_number = 1
largest_number = 5


# Feature 1: This lets the player pick a difficulty.
def choose_difficulty():
    print("\nCHOOSE YOUR DIFFICULTY")
    print("1. Easy   - 10 tries")
    print("2. Medium - 7 tries")
    print("3. Hard   - 5 tries")

    for turn in count(1):
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Oops! Please enter 1, 2, or 3.")


# This runs the game.
def play_game():
    print("====================================")
    print("          CRACK THE CODE")
    print("====================================")
    print("Guess", code_length, "different numbers.")
    print("Use numbers from", smallest_number, "to", largest_number)
    print("Enter the numbers together or with spaces.")
    print("Type 'hint' to get a new clue.")
    print("Hints and invalid guesses do not use a try.")
    print("====================================")

    max_attempts = choose_difficulty()

    # Feature 2: This makes a new random code each game.
    secret_code = random.sample(
        range(smallest_number, largest_number + 1), code_length
    )

    # This list holds the player's guess.
    guess = []

    # Feature 3: This makes hints that match the random code.
    hints = []

    for i in range(code_length):
        for number in range(smallest_number, largest_number + 1):
            if secret_code[i] < number:
                hints.append(
                    "The number in position " + str(i + 1)
                    + " is less than " + str(number) + "."
                )
            elif secret_code[i] > number:
                hints.append(
                    "The number in position " + str(i + 1)
                    + " is greater than " + str(number) + "."
                )

    # This keeps track of the player's tries.
    attempts = 0

    # This keeps asking for input until the game ends.
    for turn in count(1):
        print("\nTry", attempts + 1, "of", max_attempts)
        entry = input("Your guess: ").strip().lower().replace(" ", "")

        # This gives a hint and removes it so it cannot repeat.
        if entry == "hint":
            if len(hints) > 0:
                hint = random.choice(hints)
                print("\nHINT:", hint)
                hints.remove(hint)
            else:
                print("You have seen all the hints!")

        # This checks that the guess has the right length.
        elif len(entry) != code_length:
            print("Please enter exactly", code_length, "numbers.")

        # This checks the numbers before counting the guess.
        else:
            guess = []
            valid = True

            for number in entry:
                if not number.isdecimal():
                    valid = False
                else:
                    value = int(number)

                    if value < smallest_number or value > largest_number:
                        valid = False
                    elif value in guess:
                        valid = False
                    else:
                        guess.append(value)

            # This shows an error without using a try.
            if not valid:
                print(
                    "Use numbers from", smallest_number, "to", largest_number
                )
                print("Do not repeat any numbers.")

            # This checks a valid guess.
            else:
                attempts = attempts + 1
                correct_values = 0
                correct_positions = 0

                for i in range(code_length):
                    if guess[i] in secret_code:
                        correct_values = correct_values + 1

                    if guess[i] == secret_code[i]:
                        correct_positions = correct_positions + 1

                # This shows the results of the guess.
                print("\n====================================")
                print("           GUESS RESULTS")
                print("====================================")
                print("Your guess:", entry)
                print("------------------------------------")
                print("Correct values:", correct_values)
                print("Numbers in the right spot:", correct_positions)
                print(
                    "Right numbers, wrong spot:",
                    correct_values - correct_positions
                )
                print("Numbers not in the code:", code_length - correct_values)
                print("------------------------------------")
                print("Tries used:", attempts)
                print("Tries left:", max_attempts - attempts)
                print("====================================")

                # This ends the game if the player wins.
                if guess == secret_code:
                    print("\nYOU CRACKED THE CODE!")
                    print("Tries used:", attempts)
                    print("The secret code was:", secret_code)
                    return

                # This ends the game when there are no tries left.
                elif attempts == max_attempts:
                    print("\nGAME OVER! You ran out of tries.")
                    print("The secret code was:", secret_code)
                    return

                # This gives the player a message about their guess.
                elif correct_values == code_length:
                    print("You found all the numbers!")
                    print("Try putting them in a different order.")
                else:
                    print("Use these clues to plan your next guess!")


# This starts the game.
play_game()
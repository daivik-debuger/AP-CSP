# Name: Daivik Lakkisetty Naga
# Program Name: Crack the Code
# Program Date: October 19, 2026
# Program Summary: Guess a secret code before running out of tries.

import random

# This shows the title and rules.
print("====================================")
print("          CRACK THE CODE")
print("====================================")
print("Guess 4 different numbers from 1 to 5.")
print("Enter your guess like 1234.")
print("Type 'hint' to get a clue.")
print("Hints do not use a try.")
print("====================================")

# Feature 1: The player picks a difficulty.
print("\nCHOOSE YOUR DIFFICULTY")
print("1. Easy   - 10 tries")
print("2. Medium - 7 tries")
print("3. Hard   - 5 tries")

while True:
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        max_attempts = 10
        break
    elif choice == "2":
        max_attempts = 7
        break
    elif choice == "3":
        max_attempts = 5
        break
    else:
        print("Oops! Please enter 1, 2, or 3.")

# Feature 2: This picks 4 different random numbers.
secret_code = random.sample(range(1, 6), 4)

# This list holds the player's guess.
guess = []

# Feature 3: This makes clues about the secret code.
hints = []

for i in range(4):
    for number in range(1, 6):
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

# These keep track of the tries and if the player won.
attempts = 0
won = False

# This keeps the game going while there are tries left.
while attempts < max_attempts:
    print("\nTry", attempts + 1, "of", max_attempts)
    entry = input("Your guess: ").strip().lower().replace(" ", "")

    # This picks a hint and removes it so it cannot repeat.
    if entry == "hint":
        if len(hints) > 0:
            hint = random.choice(hints)
            print("\nHINT:", hint)
            hints.remove(hint)
        else:
            print("You have seen all the hints!")

        continue

    # The guess needs to have exactly 4 numbers.
    if len(entry) != 4:
        print("Oops! Please enter exactly 4 numbers.")
        continue

    # This checks for wrong numbers and repeats.
    guess = []
    valid = True

    for number in entry:
        if number not in "12345":
            valid = False
        elif int(number) in guess:
            valid = False
        else:
            guess.append(int(number))

    # An invalid guess does not use a try.
    if not valid:
        print("Oops! Use numbers 1 to 5 with no repeats.")
        continue

    # This counts the player's valid guess.
    attempts = attempts + 1

    # These start at zero for each guess.
    correct_values = 0
    correct_positions = 0

    # This checks each number and its spot.
    for i in range(4):
        if guess[i] in secret_code:
            correct_values = correct_values + 1

        if guess[i] == secret_code[i]:
            correct_positions = correct_positions + 1

    # This shows the results of the player's guess.
    print("\n====================================")
    print("           GUESS RESULTS")
    print("====================================")
    print("Your guess:", entry)
    print("------------------------------------")
    print("Correct values:", correct_values)
    print("Numbers in the right spot:", correct_positions)
    print("Right numbers, wrong spot:", correct_values - correct_positions)
    print("Numbers not in the code:", 4 - correct_values)
    print("------------------------------------")
    print("Tries used:", attempts)
    print("Tries left:", max_attempts - attempts)
    print("------------------------------------")

    # This gives the player a message about their guess.
    if correct_positions == 4:
        print("Perfect! Every number is in the right spot!")
    elif attempts == max_attempts:
        print("That was your last try!")
    elif correct_values == 4:
        print("You found all 4 numbers!")
        print("Try putting them in a different order.")
    else:
        print("Use these clues to plan your next guess!")

    print("====================================")

    # The player wins when the whole guess matches.
    if guess == secret_code:
        won = True
        print("\n====================================")
        print("        YOU CRACKED THE CODE!")
        print("You won in", attempts, "tries!")
        print("The secret code was:", secret_code)
        print("====================================")
        break

# This shows the secret code if the player loses.
if not won:
    print("\n====================================")
    print("              GAME OVER")
    print("You ran out of tries! You lose.")
    print("The secret code was:", secret_code)
    print("====================================")
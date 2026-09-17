import random

def guess_the_number():
    
    secret_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10. Can you guess it?")
    
    guessed_correctly = False

    while not guessed_correctly:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed the right number ({secret_number})!\n")
            guessed_correctly = True
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

   
    name = input("What your name? (Type 'end' to stop): ")

    while name.lower() != "end":
        print(f"Hello, {name}!")
        name = input("What is your name? (Type 'end' to stop): ")

    print("Goodbye you !")

if __name__ == "__main__":
    guess_the_number()


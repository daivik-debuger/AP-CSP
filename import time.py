import time

print("--- PAPER FORTUNE TELLER --- \n")

print("Outer colors: [Red, Blue, Green, Yellow]")
color = input("Choose a color: ").strip().lower()

print("\nSpelling it out...")
for letter in color:
    print(f"-> {letter.upper()}")
    time.sleep(0.4)

print("\nVisible numbers: 1, 2, 5, 6")
num1 = int(input("Pick a number: "))

print(f"\nCounting to {num1}...")
for i in range(1, num1 + 1):
    print(f"-> {i}")
    time.sleep(0.4)

print("\nFinal numbers to open: 1, 2, 3, 4, 5, 6, 7, 8")
choice = int(input("Pick a final number to lift the flap: "))

print("\nYOUR FORTUNE IS:")

if choice == 1:
    print("You will find money on the ground soon!")

elif choice == 2:
    print("A big surprise awaits you tomorrow mu ha ha ha !")

elif choice == 3:
    print("You will not ace your next challenge !")

elif choice == 4:
    print("You will have a good week!")
    
    print("Good news is not heading your way!")

elif choice == 6:
    print("You will go on an unexpected adventure!")

elif choice == 7:
    print("Your wish is not going to come true!")

elif choice == 8:
    print("Someone is going to tell you a secret!")

else:
    print(" Invalid number! The fortune teller has closed.")

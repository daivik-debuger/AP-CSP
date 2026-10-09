import time

def print_slow(text):
    """Prints text line by line with a small delay for dramatic effect."""
    print(text)
    time.sleep(0.03)

def start_game():
    lives = 3
    current_room = "science_lab"
    
    print_slow("=======================================")
    print_slow("      WELCOME TO THE SCHOOL ESCAPE     ")
    print_slow("=======================================\n")
    print_slow("You find yourself locked inside the school after hours.")
    print_slow("You must navigate through 3 rooms to escape.")
    print_slow("Choose wisely... one wrong move will cost you a life!")
    print_slow("You have 3 lives. Good luck!\n")
    
    
    while lives > 0:
        print_slow(f"\n[LIVES REMAINING: {lives}]")
        
        
        if current_room == "science_lab":
            print_slow("--- ROUTE 1: THE SCIENCE LAB ---")
            print_slow("You are locked in the chemistry lab.")
            print_slow("There are two chemical recipes on the board that might open a hidden door.")
            print_slow("Option A: Mix the blue liquid and yellow powder.")
            print_slow("Option B: Mix the red liquid and green crystal.")
            
            choice = input("Do you choose A or B? ").strip().upper()
            
            if choice == 'A':
                print_slow("\nSUCCESS! The mixture creates a harmless smoke screen.")
                print_slow("It triggers the smoke detector, which opens a secret passage behind the whiteboard!")
                current_room = "library"
            elif choice == 'B':
                print_slow("\nBOOM! The mixture causes a massive, violent reaction.")
                print_slow("Toxic green slime dissolves everything in the room... including you!")
                lives -= 1
            else:
                print_slow("Invalid choice. Try again.")
                
        elif current_room == "library":
            print_slow("\n--- ROUTE 2: THE HAUNTED LIBRARY ---")
            print_slow("You enter the pitch-black library.")
            print_slow("You see two books sticking out of a bookshelf.")
            print_slow("Option A: Pull 'A History of Hidden Passages'.")
            print_slow("Option B: Pull 'The Art of Silence'.")
            
            choice = input("Do you choose A or B? ").strip().upper()
            
            if choice == 'A':
                print_slow("\nSUCCESS! You hear a loud click.")
                print_slow("The bookshelf swings open, revealing stairs leading down to the cafeteria.")
                current_room = "cafeteria"
            elif choice == 'B':
                print_slow("\nOH NO! The floor beneath you vanishes.")
                print_slow("You fall into a pit of giant, hungry mutant bookworms!")
                lives -= 1
            else:
                print_slow("Invalid choice. Try again.")
                
        elif current_room == "cafeteria":
            print_slow("\n--- ROUTE 3: THE CAFETERIA ---")
            print_slow("You made it to the cafeteria, but the exit is padlocked.")
            print_slow("You need to find a way out.")
            print_slow("Option A: Crawl through the dark serving hatch into the kitchen.")
            print_slow("Option B: Use a rusty crowbar to pry open the main double doors.")
            
            choice = input("Do you choose A or B? ").strip().upper()
            
            if choice == 'A':
                print_slow("\nSUCCESS! You crawl into the back kitchen.")
                print_slow("Digging through a pot of yesterday's soup, you find the exit key!")
                print_slow("You unlock the back door and run into the night...")
                print_slow("\n=======================================")
                print_slow("             YOU ESCAPED!              ")
                print_slow("=======================================")
                print_slow(f"Congratulations! You survived with {lives} lives remaining!\n")
                break
            elif choice == 'B':
                print_slow("\nBEEP BEEP BEEP! The doors were rigged!")
                print_slow("You triggered the school's lockdown defense system.")
                print_slow("Laser beams shoot from the ceiling and vaporize you!")
                lives -= 1
            else:
                print_slow("Invalid choice. Try again.")
                
    if lives == 0:
        print_slow("\n=======================================")
        print_slow("              GAME OVER                ")
        print_slow("=======================================")
        print_slow("You ran out of lives. Better luck next time!\n")
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry == 'yes' or retry == 'y':
            print("\n")
            start_game()
        else:
            print("Thanks for playing!")

if __name__ == "__main__":
    start_game()

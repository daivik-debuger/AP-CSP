def choose(prompt, options):
    answer = input(prompt).strip()
    if answer in options:
        return answer
    print("That choice is not available. You did not lose a life.")
    return choose("Type " + " or ".join(options) + ": ", options)


items = ["Flashlight", "Gas mask", "Rope", "Crowbar", "Map", "Keycard"]
lives = 3
won = False

print("\n========================================")
print("          ESCAPE THE BUNKER")
print("========================================")
print("You wake up in an underground emergency shelter.")
print("An alarm warns that the shelter is no longer safe.")
print("Your goal: get through 5 rooms and reach the surface.")
print("\nHOW TO PLAY")
print("Type the number beside your choice, then press Enter.")
print("Read each room carefully. The descriptions contain clues.")
print("You start with 3 lives. A deadly choice costs 1 life.")
print("After a death, restart at room 1 and choose your items again.")
print("Escape to win. Lose all 3 lives and the game ends.")

for attempt in range(3):
    inventory = []
    available = ["1", "2", "3", "4", "5", "6"]
    print("\n========== PACK YOUR BAG ==========")
    print("A sign reads: TOXIC GAS AHEAD. BRING A GAS MASK.")
    print("Pick 3 different items by entering one number at a time.")
    print("The gas mask protects you. The flashlight and map give clues.")
    print("The other items are spare equipment for this adventure.")
    for number in range(6):
        print(str(number + 1) + ". " + items[number])

    for pick in range(3):
        print("\nItems still to choose:", 3 - pick)
        print("Available item numbers: " + ", ".join(available))
        number = choose("Type an item number: ", available)
        item = items[int(number) - 1]
        inventory.append(item)
        available.remove(number)
        print(item + " added!")

    for level in range(1, 6):
        print("\n----------------------------------------")
        print("ROOM", level, "OF 5  |  LIVES LEFT:", lives)
        print("YOU ARE CARRYING: " + ", ".join(inventory))
        print("----------------------------------------")
        safe = True

        if level == 1:
            print("THE TWO TUNNELS")
            print("Two tunnels lead away from the entrance.")
            print("Exposed wires hang over a flooded passage.")
            if "Map" in inventory:
                print("Your map marks the maintenance tunnel as a safe route.")
            print("1. Maintenance tunnel\n2. Flooded passage")
            if choose("Which tunnel? Type 1 or 2: ", ["1", "2"]) == "2":
                print("You step into electrified water!")
                safe = False
            else:
                print("The tunnel leads to a locked door.")

        elif level == 2:
            print("THE LOCKED DOOR")
            print("A keypad controls the door to the generator room.")
            print("Its screen reads: 2, 4, 6, ?")
            print("Enter the next number in the pattern to unlock the door.")
            print("Warning: a wrong answer activates a deadly security trap.")
            if input("Enter the next number: ").strip() == "8":
                print("ACCESS GRANTED. The door opens.")
            else:
                print("Wrong code! The security trap fires before you can escape.")
                safe = False

        elif level == 3:
            print("THE GENERATOR ROOM")
            print("A damaged generator throws sparks across the room.")
            print("You must reach the door on the other side.")
            if "Flashlight" in inventory:
                print("Your flashlight reveals a sign: SAFE WALKWAY ALONG WALL.")
            print("1. Marked walkway\n2. Shortcut beside the generator")
            if choose("Which route? Type 1 or 2: ", ["1", "2"]) == "2":
                print("The generator explodes as you pass!")
                safe = False
            else:
                print("You safely reach the next room.")

        elif level == 4:
            print("THE GAS CHAMBER")
            print("Toxic gas fills the chamber.")
            print("The only way forward is through this room.")
            input("Press Enter to check your bag for a gas mask: ")
            if "Gas mask" in inventory:
                print("You put on your gas mask and cross safely.")
            else:
                print("Without a gas mask, you cannot survive!")
                safe = False

        elif level == 5:
            print("THE FINAL EXIT")
            print("You have reached the bottom of an exit shaft.")
            print("Daylight shines above a ladder.")
            print("1. Climb the ladder\n2. Elevator marked OUT OF ORDER")
            if choose("How will you escape? Type 1 or 2: ", ["1", "2"]) == "2":
                print("The elevator cables snap!")
                safe = False
            else:
                print("You climb the ladder and push open the hatch to the surface.")
                won = True

        if not safe:
            lives -= 1
            print("\nYou died and lost 1 life. Lives remaining:", lives)
            if lives > 0:
                input("Press Enter to restart at room 1 with a new bag: ")
            break
        elif not won:
            input("Room complete! Press Enter to enter the next room: ")

    if won:
        break

print("\n========================================")
if won:
    print("     YOU ESCAPED! FRESH AIR AT LAST!")
    print("Lives remaining:", lives)
else:
    print("       GAME OVER. NO LIVES LEFT.")
    print("Run the game again to try a different set of choices.")
print("========================================")

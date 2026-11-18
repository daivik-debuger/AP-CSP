# Escape the Bunker
# Name: Daivik Lakkisetty Naga
# Date: 11/12/2026
# AP CSP Period 1

# Function to get a valid choice from the player
def choose(prompt, options):
    ans = input(prompt).strip().lower()
    while ans not in options:
        print("Invalid choice! Choose: " + " or ".join(options))
        ans = input(prompt).strip().lower()
    return ans

# Game setup variables
items = ["Flashlight", "Gas Mask", "Medkit", "Crowbar", "Bunker Map", "Keycard"]
lives = 10
win = False

# Print game introduction
print("\n==================================================")
print("             ESCAPE THE BUNKER")
print("==================================================")
print("You awaken deep inside a collapsing underground bunker.")
print("Your objective: Navigate through 5 sectors and reach the surface ALIVE!")
print("You start with 10 lives. Fatal mistakes cost 1 life.")

# Main game loop that runs until you win or lose all lives
while not win and lives > 0:
    inventory = []
    options_indices = [str(i + 1) for i in range(len(items))]

    # Let the player pick 3 items out of 6
    print("\n" + "=" * 50)
    print("               PACK YOUR BACKPACK")
    print("=" * 50)
    print("Select 3 distinct items from the armory:")
    for i in range(len(items)):
        print(str(i + 1) + ". " + items[i])

    for pick in range(3):
        print("\nPicks remaining:", 3 - pick)
        print("Available numbers: " + ", ".join(options_indices))
        selected_idx = choose("Enter item number: ", options_indices)
        chosen_item = items[int(selected_idx) - 1]
        inventory.append(chosen_item)
        options_indices.remove(selected_idx)
        print("Added [" + chosen_item + "] to your backpack.")

    # Data for all 5 levels
    levels = [
        {
            "num": 1,
            "type": "path",
            "title": "LEVEL 1: THE SPLIT TUNNEL (PATH)",
            "desc": "Two dark tunnels stretch out before you.\n1. Left: Narrow maintenance duct with rattling pipes.\n2. Right: Flooded passageway with dangling electrical cables.",
            "clue_item": "Bunker Map",
            "clue": "The map marks the Left duct as structurally dry and safe.",
            "safe": ["1", "left"],
            "death": "You stepped into the water! A live electrical cable electrocuted you.",
            "success": "You crawled safely through the duct to the next area."
        },
        {
            "num": 2,
            "type": "extra",
            "title": "LEVEL 2: THE ALCHEMY & MED-BAY (EXTRA FEATURE)",
            "desc": "You find a lab with two glowing potions:\n1. Blue Elixir (shimmers with blue restorative light)\n2. Red Serum (hisses and bubbles with dark fumes)",
            "loot": "Adrenaline Shot"
        },
        {
            "num": 3,
            "type": "path",
            "title": "LEVEL 3: THE GENERATOR VAULT (PATH)",
            "desc": "A nuclear reactor turbine is rumbling with intense pressure.\n1. Left: Upper steel catwalk running along the ceiling.\n2. Right: Narrow shortcut right beside the vibrating turbine.",
            "clue_item": "Flashlight",
            "clue": "Your beam illuminates a hazard sign: 'DANGER: HIGH PRESSURE STEAM LEAK'.",
            "safe": ["1", "left"],
            "death": "A high-pressure steam pipe ruptured as you ran past!",
            "success": "You crossed the elevated catwalk safely."
        },
        
        {
            "num": 4,
            "type": "item_check",
            "title": "LEVEL 4: DECONTAMINATION AIRLOCK (INVENTORY CHECK)",
            "desc": "The blast doors seal tight! Poisonous green chlorine gas fills the air.",
            "required_item": "Gas Mask",
            "success": "You put on your Gas Mask and breathe clean filtered air.",
            "death": "You do not have a Gas Mask! The toxic gas overwhelms you."
        },
        {
            "num": 5,
            "type": "path",
            "title": "LEVEL 5: THE SURFACE ACCESS SHAFT (FINAL PATH)",
            "desc": "Daylight beams down from above!\n1. Left: Reinforced steel ladder bolted to the wall.\n2. Right: Decaying cable elevator marked 'OUT OF ORDER'.",
            "clue_item": "",
            "clue": "",
            "safe": ["1", "left"],
            "death": "The elevator cables snapped and plummeted down the shaft!",
            "success": "You climbed the ladder to the surface into the sunlight!"
        }
    ]

    # Play through each level one by one
    for room in levels:
        print("\n" + "-" * 50)
        print("LEVEL " + str(room["num"]) + " OF 5 | LIVES REMAINING: " + str(lives))
        print("YOUR INVENTORY: " + ", ".join(inventory))
        print("-" * 50)

        safe = True

        # Handle path levels (Levels 1, 3, and 5)
        if room["type"] == "path":
            print(room["title"])
            print(room["desc"])
            if room["clue_item"] in inventory:
                print(">> CLUE (" + room["clue_item"] + "): " + room["clue"])
            decision = choose("Which path do you choose? (1/2 or left/right): ", ["1", "2", "left", "right"])
            if decision not in room["safe"]:
                print("\n[!] " + room["death"])
                safe = False
            else:
                print("\n[+] " + room["success"])
                if room["num"] == 5:
                    win = True

        # Handle extra room with potions and loot (Level 2)
        elif room["type"] == "extra":
            print(room["title"])
            print(room["desc"])
            potion = choose("Which potion do you drink? (1 for Blue / 2 for Red): ", ["1", "2", "blue", "red"])
            if potion in ["1", "blue"]:
                lives += 2
                print("\n[+] REJUVENATION: You drank the blue elixir and gained +2 lives! Lives: " + str(lives))
            else:
                lives -= 1
                print("\n[-] POISON: Acidic liquid burned your throat! You lost 1 life! Lives: " + str(lives))
                if lives <= 0:
                    safe = False

            if safe:
                print("\nYou also found an [" + room["loot"] + "] on the counter.")
                pickup = choose("Add [" + room["loot"] + "] to inventory? (yes/no): ", ["yes", "no", "y", "n"])
                if pickup in ["yes", "y"]:
                    inventory.append(room["loot"])
                    print("-> Added [" + room["loot"] + "] to your inventory!")

        # Handle inventory check room (Level 4)
        elif room["type"] == "item_check":
            print(room["title"])
            print(room["desc"])
            input("Press Enter to check your backpack for safety gear...")
            if room["required_item"] in inventory:
                print("\n[+] INVENTORY CHECK SUCCESS: " + room["success"])
            else:
                print("\n[!] INVENTORY CHECK FAILED: " + room["death"])
                safe = False

        # If player died, lose 1 life and restart from the beginning
        if not safe:
            lives -= 1
            print("\n" + "!" * 50)
            print("YOU DIED! You lost 1 life.")
            print("Lives remaining: " + str(lives))
            print("!" * 50)
            if lives > 0:
                input("Press Enter to return to the bunker entrance and try again: ")
            break
        elif not win:
            input("\nRoom cleared! Press Enter to proceed to the next room: ")

# Final win or game over screens
print("\n" + "=" * 50)
if win:
    print("                 YOU ESCAPED! YOU WIN!")
    print("=" * 50)
    print("Congratulations! You survived and reached the surface.")
    print("Remaining Lives: " + str(lives))
    print("Final Items: " + ", ".join(inventory))
else:
    print("            GAME OVER: OUT OF LIVES!")
    print("=" * 50)
    print("The bunker collapsed entirely. You did not make it out.")
print("=" * 50 + "\n")

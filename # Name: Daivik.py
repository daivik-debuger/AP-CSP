# Name: Daivik
# Program Summary: Lets the user view, add, remove, and search for songs.

# These lists keep the songs and their times.
songs = [
    "Lose My Mind", "Just Keep Watching", "Drive", "Messy",
    "Bad as I Used To Be", "Blinding Lights", "Levitating",
    "As It Was", "Believer", "Shape of You"
]

# These are the song times in seconds. They are approximate.
durations = [209, 142, 190, 179, 227, 200, 203, 167, 204, 233]


# This shows minutes and seconds.
def show_duration(seconds):
    minutes = seconds // 60
    leftover_seconds = seconds % 60
    if leftover_seconds < 10:
        return str(minutes) + ":0" + str(leftover_seconds)
    else:
        return str(minutes) + ":" + str(leftover_seconds)


# This prints the songs and the total time.
def display_playlist():
    print("\n---------- MY PLAYLIST ----------")
    if len(songs) == 0:
        print("There are no songs yet.")
    else:
        print("No.  Song                          Time")
        print("---------------------------------------")
        total = 0
        for i in range(len(songs)):
            number = str(i + 1) + "."
            print(number.ljust(5) + songs[i].ljust(30) + "  " +
                  show_duration(durations[i]))
            total += durations[i]
        print("---------------------------------------")
        print("Number of songs:", len(songs))
        print("Total time:", show_duration(total))


# This loop keeps the menu running.
while True:
    print("\n---------- SONG MENU ----------")
    print("1. Show my playlist")
    print("2. Longest song time")
    print("3. Shortest song time")
    print("4. Longest song name")
    print("5. Shortest song name")
    print("6. Add a song")
    print("7. Remove a song")
    print("8. Search for a song")
    print("9. Show final playlist and exit")

    choice = input("Choose an option (1-9): ").strip()

    # Check if the choice is 1 to 9.
    if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        print("Invalid choice. Enter a number from 1 to 9.")
        continue

    # Show the final list and quit.
    if choice == "9":
        display_playlist()
        print("Goodbye!")
        break

    # Check if the song list is empty.
    if len(songs) == 0 and choice != "6":
        print("The playlist is empty. Choose option 6 to add a song.")
        continue

    # Show all songs.
    if choice == "1":
        display_playlist()

    # Find the longest or shortest song.
    elif choice == "2" or choice == "3":
        best = 0
        for i in range(len(durations)):
            if choice == "2" and durations[i] > durations[best]:
                best = i
            elif choice == "3" and durations[i] < durations[best]:
                best = i
        print(songs[best] + " - " + show_duration(durations[best]))

    # Find the longest or shortest song name.
    # Spaces count. If two names tie, show the first one.
    elif choice == "4" or choice == "5":
        best = 0
        for i in range(len(songs)):
            if choice == "4" and len(songs[i]) > len(songs[best]):
                best = i
            elif choice == "5" and len(songs[i]) < len(songs[best]):
                best = i
        print(songs[best] + " (" + str(len(songs[best])) + " characters)")

    # Add a new song.
    elif choice == "6":
        new_song = input("Enter the song title: ").strip()

        # Don't add an empty song.
        if new_song == "":
            print("The song title cannot be blank.")
            continue

        # Check if the song is already there.
        duplicate = False
        for song in songs:
            if song.lower() == new_song.lower():
                duplicate = True

        if duplicate:
            print("That song is already in the playlist.")
            continue

        # Keep asking until you get a valid time.
        while True:
            duration_text = input("Enter duration in seconds (example: 180): ").strip()
            try:
                new_duration = int(duration_text)
                if new_duration > 0:
                    break
                else:
                    print("Duration must be greater than zero.")
            except ValueError:
                print("Please enter a whole number of seconds.")

        songs.append(new_song)
        durations.append(new_duration)
        print("Song added! Updated playlist:")
        display_playlist()

    # Remove the song.
    elif choice == "7":
        title = input("Enter the full song title to remove: ").strip()
        if title == "":
            print("The song title cannot be blank.")
            continue

        position = -1
        for i in range(len(songs)):
            if songs[i].lower() == title.lower():
                position = i

        if position == -1:
            print("That song was not found.")
        else:
            songs.pop(position)
            durations.pop(position)
            print("Song and duration removed! Updated playlist:")
            display_playlist()

    # Search for a word in the song names.
    elif choice == "8":
        word = input("Enter a word to search for: ").strip().lower()
        if word == "":
            print("The search word cannot be blank.")
            continue

        found = False
        for i in range(len(songs)):
            if word in songs[i].lower():
                print(songs[i] + " - " + show_duration(durations[i]))
                found = True

        if not found:
            print("No songs contain that word.")
            
# Name: Daivik

# Song names.

songs = [
    "Lose My Mind", "Just Keep Watching", "Drive", "Messy",
    "Bad as I Used To Be", "Blinding Lights", "Levitating",
    "As It Was", "Believer", "Shape of You"
]

# Song times in seconds.
durations = [209, 142, 190, 179, 227, 200, 203, 167, 204, 233]


# Chosen songs.
chosen_songs = []


# Show minutes and seconds.
def show_duration(seconds):
    minutes = seconds // 60
    leftover_seconds = seconds % 60
    if leftover_seconds < 10:
        return str(minutes) + ":0" + str(leftover_seconds)
    else:
        return str(minutes) + ":" + str(leftover_seconds)


# Show songs and total time.
def display_playlist():
    print("\n---------- SONG LIBRARY ----------")
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


# Show chosen songs.
def display_chosen():
    print("\n---------- MY FINAL PLAYLIST ----------")
    if len(chosen_songs) == 0:
        print("You have not chosen any songs. Use option 10 to choose songs.")
    else:
        print("No.  Song                          Time")
        print("---------------------------------------")
        total = 0
        for i in range(len(chosen_songs)):
            position = songs.index(chosen_songs[i])
            number = str(i + 1) + "."
            print(number.ljust(5) + chosen_songs[i].ljust(30) + "  " +
                  show_duration(durations[position]))
            total += durations[position]
        print("---------------------------------------")
        print("Number of songs:", len(chosen_songs))
        print("Total time:", show_duration(total))


# Repeat the menu.
while True:
    print("\n---------- SONG MENU ----------")
    print("1. Show all songs in the library")
    print("2. Longest song time")
    print("3. Shortest song time")
    print("4. Longest song name")
    print("5. Shortest song name")
    print("6. Add a new song to the library")
    print("7. Remove a song from the library")
    print("8. Search for a song")
    print("9. Show final playlist and exit")
    print("10. Choose a song for my playlist")

    choice = input("Choose an option (1-10): ").strip()

    # Check the menu choice.
    if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print("Invalid choice. Enter a number from 1 to 10.")
        continue

    # Show chosen songs and quit.
    if choice == "9":
        display_chosen()
        print("Goodbye!")
        break

    # Check for an empty list.
    if len(songs) == 0 and choice != "6":
        print("The playlist is empty. Choose option 6 to add a song.")
        continue

    # Show all songs.
    if choice == "1":
        display_playlist()

    # Find the longest or shortest time.
    elif choice == "2" or choice == "3":
        best = 0
        for i in range(len(durations)):
            if choice == "2" and durations[i] > durations[best]:
                best = i
            elif choice == "3" and durations[i] < durations[best]:
                best = i
        print(songs[best] + " - " + show_duration(durations[best]))

    # Find the longest or shortest name.
    
    # Count spaces. Show the first name if tied.
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

        # Check for an empty name.
        if new_song == "":
            print("The song title cannot be blank.")
            continue

        # Check for repeats.
        duplicate = False
        for song in songs:
            if song.lower() == new_song.lower():
                duplicate = True

        if duplicate:
            print("That song is already in the library. Use option 10 to choose it.")
            continue

        # Check the song time.
        while True:
            duration_text = input("Enter duration in seconds (example: 180): ").strip()
            try:
                new_duration = int(duration_text)
                if new_duration > 0:
                    break
                else:
                    print("Duration must be greater than zero.")
            except ValueError:
                print("Enter a whole number of seconds.")

        songs.append(new_song)
        durations.append(new_duration)
        print("Song added! Updated library:")
        display_playlist()

    # Remove the song and its time.
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
            # Remove it from chosen songs too.
            if songs[position] in chosen_songs:
                chosen_songs.remove(songs[position])
            songs.pop(position)
            durations.pop(position)
            print("Song and duration removed! Updated library:")
            display_playlist()

    # Search for a word.
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


    # Choose a song.
    elif choice == "10":
        title = input("Enter the full song title to choose: ").strip()
        if title == "":
            print("The song title cannot be blank.")
            continue

        position = -1
        for i in range(len(songs)):
            if songs[i].lower() == title.lower():
                position = i

        if position == -1:
            print("That song was not found. Use option 1 to see the library.")
        elif songs[position] in chosen_songs:
            print("You already chose that song.")
        else:
            chosen_songs.append(songs[position])
            print("Song chosen!")
            display_chosen()

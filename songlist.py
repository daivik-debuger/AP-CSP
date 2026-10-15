# Name:  Made by Daivik

# Starting song names.

library_songs = [
    "Lose My Mind", "Just Keep Watching", "Drive", "Messy",
    "Bad as I Used To Be", "Blinding Lights", "Levitating",
    "As It Was", "Believer", "Shape of You"
]

# Song times in seconds .
library_durations = [209, 142, 190, 179, 227, 200, 203, 167, 204, 233]


# Your playlist starts empty.
songs = []
durations = []


# Show minutes and seconds.
def show_duration(seconds):
    minutes = seconds // 60
    leftover_seconds = seconds % 60
    if leftover_seconds < 10:
        return str(minutes) + ":0" + str(leftover_seconds)
    else:
        return str(minutes) + ":" + str(leftover_seconds)


# Show songs and total time.
def display_playlist(song_list, time_list, heading):
    print("\n---------- " + heading + " ----------")
    if len(song_list) == 0:
        print("There are no songs yet.")
    else:
        print("No.  Song                          Time")
        print("---------------------------------------")
        total = 0
        for i in range(len(song_list)):
            number = str(i + 1) + "."
            print(number.ljust(5) + song_list[i].ljust(30) + "  " +
                  show_duration(time_list[i]))
            total += time_list[i]
        print("---------------------------------------")
        print("Number of songs:", len(song_list))
        print("Total time:", show_duration(total))


# Repeat the menu.
while True:
    print("\n---------- SONG MENU ----------")
    print("1. Show all available songs and times")
    print("2. Longest available song time")
    print("3. Shortest available song time")
    print("4. Longest available song name")
    print("5. Shortest available song name")
    print("6. Add a given song to my playlist")
    print("7. Add my own song and time")
    print("8. Search my playlist")
    print("9. Show final playlist and exit")
    print("10. Remove a song from my playlist")

    choice = input("Choose an option (1-10): ").strip()

    # Check the menu choice.
    if choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        print("Invalid choice. Enter a number from 1 to 10.")
        continue

    # Show the final playlist and quit.
    if choice == "9":
        display_playlist(songs, durations, "FINAL PLAYLIST")
        print("Goodbye!")
        break

    # Show all songs.
    if choice == "1":
        display_playlist(library_songs, library_durations, "AVAILABLE SONGS")

    # Find the longest or shortest time.
    elif choice == "2" or choice == "3":
        best = 0
        for i in range(len(library_durations)):
            if choice == "2" and library_durations[i] > library_durations[best]:
                best = i
            elif choice == "3" and library_durations[i] < library_durations[best]:
                best = i
        print(library_songs[best] + " - " + show_duration(library_durations[best]))

    # Find the longest or shortest name.

    
    # Count spaces. Show the first name if tied.
    elif choice == "4" or choice == "5":
        best = 0
        for i in range(len(library_songs)):
            if choice == "4" and len(library_songs[i]) > len(library_songs[best]):
                best = i
            elif choice == "5" and len(library_songs[i]) < len(library_songs[best]):
                best = i
        print(library_songs[best] + " (" + str(len(library_songs[best])) + " characters)")

    # Add a song from the given list.
    elif choice == "6":
        display_playlist(library_songs, library_durations, "AVAILABLE SONGS")
        title = input("Enter the full song name: ").strip()
        if title == "":
            print("The song name cannot be blank.")
            continue

        position = -1
        for i in range(len(library_songs)):
            if library_songs[i].lower() == title.lower():
                position = i

        if position == -1:
            print("That song is not in the given list. Use option 7 for your own song.")
        elif library_songs[position] in songs:
            print("That song is already in your playlist.")
        else:
            songs.append(library_songs[position])
            durations.append(library_durations[position])
            print("Song added!")
            display_playlist(songs, durations, "MY PLAYLIST")

    # Add your own song and time.
    elif choice == "7":
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
            print("That song is already in the playlist.")
            continue

        given_song = False
        for song in library_songs:
            if song.lower() == new_song.lower():
                given_song = True
        if given_song:
            print("That song is in the given list. Use option 6 to add it.")
            continue

        # Check the song time.
        while True:
            duration_text = input("Enter time as seconds or m:ss (180 or 3:00): ").strip()
            try:
                if ":" in duration_text:
                    minutes_text, seconds_text = duration_text.split(":")
                    minutes = int(minutes_text)
                    seconds = int(seconds_text)
                    if minutes < 0 or seconds < 0 or seconds > 59:
                        print("Use minutes and seconds from 00 to 59.")
                        continue
                    new_duration = minutes * 60 + seconds
                else:
                    new_duration = int(duration_text)
                if new_duration > 0:
                    break
                else:
                    print("Duration must be greater than zero.")
            except ValueError:
                print("Enter whole seconds or a time like 3:00.")

        songs.append(new_song)
        durations.append(new_duration)
        print("Song added! Updated playlist:")
        display_playlist(songs, durations, "MY PLAYLIST")

    # Remove the song and its time.
    elif choice == "10":
        if len(songs) == 0:
            print("Your playlist is empty. Use option 6 or 7 to add songs.")
            continue
        display_playlist(songs, durations, "MY PLAYLIST")
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
            display_playlist(songs, durations, "MY PLAYLIST")

    # Search for a word.
    elif choice == "8":
        if len(songs) == 0:
            print("Your playlist is empty. Use option 6 or 7 to add songs.")
            continue
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


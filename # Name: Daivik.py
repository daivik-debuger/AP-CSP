# Name: Daivik

# Starting song names.
library_songs = [
    "Lose My Mind", "Just Keep Watching", "Drive", "Messy",
    "Bad as I Used To Be", "Blinding Lights", "Levitating",
    "As It Was", "Believer", "Shape of You"
]

# Song times in seconds.
library_durations = [209, 142, 190, 179, 227, 200, 203, 167, 204, 233]

# Your playlist starts empty.
songs = []
durations = []


# Turn seconds into m:ss (example: 185 -> 3:05).
def show_duration(seconds):
    return str(seconds // 60) + ":" + str(seconds % 60).zfill(2)


# Show songs and total time.
def display_playlist(song_list, time_list, heading):
    print("\n---------- " + heading + " ----------")
    if len(song_list) == 0:
        print("There are no songs yet.")
        return
    print("No.  Song                          Time")
    print("---------------------------------------")
    for i in range(len(song_list)):
        number = str(i + 1) + "."
        print(number.ljust(5) + song_list[i].ljust(30) + "  " + show_duration(time_list[i]))
    print("---------------------------------------")
    print("Number of songs:", len(song_list))
    print("Total time:", show_duration(sum(time_list)))


# Find a song in a list (ignores upper/lower case). Returns -1 if not found.
def find_song(song_list, title):
    for i in range(len(song_list)):
        if song_list[i].lower() == title.lower():
            return i
    return -1


# Ask for text. Returns "" if the user typed nothing.
def ask_text(prompt):
    text = input(prompt).strip()
    if text == "":
        print("This cannot be blank.")
    return text


# Keep asking until the user types a good time (180 or 3:00).
def ask_duration():
    while True:
        text = input("Enter time as seconds or m:ss (180 or 3:00): ").strip()
        try:
            if ":" in text:
                minutes, seconds = text.split(":")
                minutes = int(minutes)
                seconds = int(seconds)
                if minutes < 0 or seconds < 0 or seconds > 59:
                    print("Use minutes and seconds from 00 to 59.")
                    continue
                total = minutes * 60 + seconds
            else:
                total = int(text)
            if total > 0:
                return total
            print("Duration must be greater than zero.")
        except ValueError:
            print("Enter whole seconds or a time like 3:00.")


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

    # 1. Show all songs.
    if choice == "1":
        display_playlist(library_songs, library_durations, "AVAILABLE SONGS")

    # 2 and 3. Longest or shortest time (first one wins a tie).
    elif choice == "2" or choice == "3":
        if choice == "2":
            i = library_durations.index(max(library_durations))
        else:
            i = library_durations.index(min(library_durations))
        print(library_songs[i] + " - " + show_duration(library_durations[i]))

    # 4 and 5. Longest or shortest name (spaces count, first one wins a tie).
    elif choice == "4" or choice == "5":
        if choice == "4":
            name = max(library_songs, key=len)
        else:
            name = min(library_songs, key=len)
        print(name + " (" + str(len(name)) + " characters)")

    # 6. Add a song from the given list.
    elif choice == "6":
        display_playlist(library_songs, library_durations, "AVAILABLE SONGS")
        title = ask_text("Enter the full song name: ")
        if title == "":
            continue
        i = find_song(library_songs, title)
        if i == -1:
            print("That song is not in the given list. Use option 7 for your own song.")
        elif find_song(songs, title) != -1:
            print("That song is already in your playlist.")
        else:
            songs.append(library_songs[i])
            durations.append(library_durations[i])
            print("Song added!")
            display_playlist(songs, durations, "MY PLAYLIST")

    # 7. Add your own song and time.
    elif choice == "7":
        title = ask_text("Enter the song title: ")
        if title == "":
            continue
        if find_song(songs, title) != -1:
            print("That song is already in the playlist.")
            continue
        if find_song(library_songs, title) != -1:
            print("That song is in the given list. Use option 6 to add it.")
            continue
        songs.append(title)
        durations.append(ask_duration())
        print("Song added! Updated playlist:")
        display_playlist(songs, durations, "MY PLAYLIST")

    # 8. Search my playlist for a word.
    elif choice == "8":
        if len(songs) == 0:
            print("Your playlist is empty. Use option 6 or 7 to add songs.")
            continue
        word = ask_text("Enter a word to search for: ").lower()
        if word == "":
            continue
        found = False
        for i in range(len(songs)):
            if word in songs[i].lower():
                print(songs[i] + " - " + show_duration(durations[i]))
                found = True
        if not found:
            print("No songs contain that word.")

    # 9. Show the final playlist and quit.
    elif choice == "9":
        display_playlist(songs, durations, "FINAL PLAYLIST")
        print("Goodbye!")
        break

    # 10. Remove a song and its time.
    elif choice == "10":
        if len(songs) == 0:
            print("Your playlist is empty. Use option 6 or 7 to add songs.")
            continue
        display_playlist(songs, durations, "MY PLAYLIST")
        title = ask_text("Enter the full song title to remove: ")
        if title == "":
            continue
        i = find_song(songs, title)
        if i == -1:
            print("That song was not found.")
        else:
            songs.pop(i)
            durations.pop(i)
            print("Song and duration removed! Updated playlist:")
            display_playlist(songs, durations, "MY PLAYLIST")

    # Anything else is not a menu option.
    else:
        print("Invalid choice. Enter a number from 1 to 10.")

# welcome to the the song playlist 
print("Welcome to the song playlist 2000!") 

def main():
    # The song selection menu will be here. 
    songs = [
        "Bohemian Rhapsody", "Stairway to Heaven", "Hotel California",
        "Imagine", "Smells Like Teen Spirit", "Sweet Child O' Mine",
        "Hey Jude", "Like a Rolling Stone", "Billie Jean", "Purple Rain"
    ]
    durations = [
        5.55, 8.02, 6.30, 
        3.03, 5.01, 5.56, 
        7.11, 6.13, 4.54, 8.41
    ]
# The main 
    
    while True:
        
        print("\n--- Song Playlist Menu ---")
        print("1. Display all the songs along with their song duration")
        print("2. Show the longest song duration")
        print("3. Show the shortest song duration")
        print("4. Show the song with the longest name")
        print("5. Show the song with the shortest name")
        print("6. Add a new song and duration to the existing lists")
        print("7. Remove a song and its duration from the existing lists")
        print("8. Search the playlist for a song with a specific word in it")
        print("9. Exit / Quit")
        
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':
            
            print("\n--- Playlist ---")
            if not songs:
                
                print("The playlist is currently empty.")
            else:
                for i in range(len(songs)):
                    print(f"{i+1}. {songs[i]} - {durations[i]} mins")
                    
        elif choice == '2':
            
            if not durations:
                
                print("The playlist is currently empty.")
            else:
                max_duration = durations[0]
                max_index = 0
                for i in range(1, len(durations)):
                    if durations[i] > max_duration:
                        max_duration = durations[i]
                        max_index = i
                print(f"\nLongest song duration: {songs[max_index]} with {max_duration} mins")
                
        elif choice == '3':
            
            if not durations:
                
                print("The playlist is currently empty.")
            else:
                min_duration = durations[0]
                min_index = 0
                for i in range(1, len(durations)):
                    if durations[i] < min_duration:
                        min_duration = durations[i]
                        min_index = i
                print(f"\nShortest song duration: {songs[min_index]} with {min_duration} mins")
                
        elif choice == '4':
            
            if not songs:
                
                print("The playlist is currently empty.")
            else:
                longest_name = songs[0]
                for song in songs:
                    if len(song) > len(longest_name):
                        longest_name = song
                print(f"\nSong with the longest name: {longest_name}")
                
        elif choice == '5':
            
            if not songs:
                
                print("The playlist is currently empty.")
            else:
                shortest_name = songs[0]
                for song in songs:
                    if len(song) < len(shortest_name):
                        shortest_name = song
                print(f"\nSong with the shortest name: {shortest_name}")
                
        elif choice == '6':
            
            new_song = input("Enter the name of the new song: ").strip()
            
            
            if not new_song:
                print("Song name cannot be empty.")
                continue
                
            duplicate = False
            for song in songs:
                if song.lower() == new_song.lower():
                    duplicate = True
                    break
            
            if duplicate:
                print("Error: This song is already in the playlist!")
                continue
                
            duration_input = input("Enter the duration of the song (e.g., 3.45): ").strip()
            
            
            try:
                new_duration = float(duration_input)
                if new_duration <= 0:
                    print("Error: Duration must be greater than 0.")
                    continue
                
                songs.append(new_song)
                durations.append(new_duration)
                print(f"Successfully added '{new_song}' to the playlist!")
            except ValueError:
                print("Error: Invalid duration format. Please enter a valid number.")
                
        elif choice == '7':
                
            if not songs:
                
                print("The playlist is already empty.")
                continue
                
            remove_song = input("Enter the exact name of the song to remove: ").strip()
            found = False
            
            
            for i in range(len(songs)):
                if songs[i].lower() == remove_song.lower():
                    removed_name = songs.pop(i)
                    durations.pop(i)
                    print(f"Successfully removed '{removed_name}' from the playlist!")
                    found = True
                    break
                    
          
            if not found:
                print("Error: Song not found in the playlist.")
                
        elif choice == '8':
            
            if not songs:
                
                print("The playlist is currently empty.")
                continue
                
            search_word = input("Enter a word to search for: ").strip().lower()
            if not search_word:
                print("Search word cannot be empty.")
                continue
                
            print(f"\n--- Search Results for '{search_word}' ---")
            found = False
            for i in range(len(songs)):
                if search_word in songs[i].lower():
                    print(f"{songs[i]} - {durations[i]} mins")
                    found = True
                    
            if not found:
                print("No songs found containing that word.")
                
        elif choice == '9':
            print("Exiting Song Playlist. Goodbye!")
            break
            
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
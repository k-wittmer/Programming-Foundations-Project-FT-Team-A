


import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"

import movies

def mark_movie_watched():

    #select an existing movie
    movie_library, selected_movie = movies.select_movie()

    if selected_movie is None:
        print("Invalid movie selection")
        return

    #display the current wacth status
    if selected_movie["watched"] == True:
        current_status = "Watched"
    else:
        current_status = "Unwatched"

    print(
               f'{selected_movie["title"]} | {current_status}')
    
    #ask user to change watch status
    print("1. Mark movie as watched")
    print("2. Mark movie as unwathced")

    choice = input("Choose function: ").strip()

    if choice == "1":
        watched_status = True

    elif choice == "2":
        watched_status = False

    else:
        print("Invalid answer")
        return

    #update the watch status of selected movie
    selected_movie["watched"] = watched_status

    #save changes to json
    movies.save_movie_library(movie_library)
       



#testing the function
if __name__ == "__main__":
    mark_movie_watched()

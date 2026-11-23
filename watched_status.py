


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

#testing the function
if __name__ == "__main__":
    mark_movie_watched()

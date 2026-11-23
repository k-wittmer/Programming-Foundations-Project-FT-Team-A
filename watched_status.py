


import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"

import movies

def mark_movie_watched():

    #select an existing movie
    selected_movie = movies.select_movie()

    if selected_movie is None:
        print("Invalid movie selection")
        return

mark_movie_watched()
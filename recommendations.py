import ui
import movies

import random
import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"

#Definition for the genre suggestion.
#It loads the library from the .json file and creates a new list with the desired genre. Then it suggests 3 random movies from that genre-based list. If there are less than 3 movies in the list, it displays only the amount of movies that are present.
def genre_suggestion():
    selected_genre = movies.add_movie_genre()
    unfiltered_library = movies.load_movie_library()
    filtered_library = []
    for movie in unfiltered_library:
        if movie["genre"] == selected_genre:
            filtered_library.append(movie)
        else:
            continue

    if len(filtered_library) >= 3:
        suggested_movies = random.sample(filtered_library, 3)
    elif len(filtered_library) == 2:
        suggested_movies = random.sample(filtered_library, 2)
    elif len(filtered_library) == 1:
        suggested_movies = random.sample(filtered_library, 1)
    else:
        suggested_movies = 0

    if suggested_movies == 0:
        print(f"There are no movies with the genre '{selected_genre}' in the movie library.")
    else:
        for movie in suggested_movies:
            watched = "Watched" if movie["watched"] else "Not watched"
            print(f"Movie-ID: {movie["ID"]} || {movie["title"]} | {movie["genre"]} | Rating: {movie["rating"]} | {watched}")


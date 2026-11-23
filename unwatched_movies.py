
### User Story
# As a user, I want to display all movies I have not watched yet so that I can easily find something new to watch.

### Acceptance Criteria
# Only unwatched movies are displayed.
# Each movie displays its title, genre, and rating.
# A message is displayed if no unwatched movies are available.

#Improvements/stuff to still work on:
## When calling fuction and printing results it looks messy(because it shows movies as raw dictionaries)
## When user has seen all movies, after the printed message the function also prints an empty list(can I get rid of this?)

import movies

import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"



def get_unwatched_movies(movies):
    unwatched_movies = []

    for movie in movies:
        if not movie["watched"]:
            unwatched_movies.append(movie)

    if not unwatched_movies:
            print("You've seen all movies")

    return unwatched_movies

if __name__ == "__main__":
     movie_library = movies.load_movie_library()
     result = get_unwatched_movies(movie_library)

     for movie in result:
          print(
               f'Title: {movie["title"]} | '
               f'Genre: {movie["genre"]} | '
               f'Rating: {movie["rating"]}')

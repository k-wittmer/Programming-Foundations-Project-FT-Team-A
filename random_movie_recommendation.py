
### User Story
# As a user, I want to receive a random movie recommendation from my library so that I can decide what to watch without searching manually.

### Acceptance Criteria
# The program randomly selects an unwatched movie.
# The recommended movie's title and genre are displayed.
# Only unwatched movies are eligible.
# A message is displayed if no unwatched movies are available.

import movies

import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"


import random
from unwatched_movies import get_unwatched_movies

def recommend_random_movie(movies):
    unwatched_movies = get_unwatched_movies(movies)

    if not unwatched_movies:
        return
    
    recommendation = random.choice(unwatched_movies) 
    return recommendation

#function testing
if __name__ == "__main__":
    movie_library = movies.load_movie_library()
    recommended_movie = recommend_random_movie(movie_library)
    if recommended_movie:
        print(
        f'Title: {recommended_movie["title"]} | '
        f'Genre: {recommended_movie["genre"]} | '
        f'Rating: {recommended_movie["rating"]}'
    )


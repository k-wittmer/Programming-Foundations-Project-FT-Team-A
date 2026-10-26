
### User Story
# As a user, I want to receive a random movie recommendation from my library so that I can decide what to watch without searching manually.

### Acceptance Criteria
# The program randomly selects an unwatched movie.
# The recommended movie's title and genre are displayed.
# Only unwatched movies are eligible.
# A message is displayed if no unwatched movies are available.


sample_library = [
{
        "ID": 1,
        "title": "Inception",
        "genre": "Science Fiction",
        "rating": 5,
        "watched": True
    },
{
        "ID": 2,
        "title": "Interstellar",
        "genre": "Science Fiction",
        "rating": 5,
        "watched": False
    },
{
        "ID": 3,
        "title": "Frozen",
        "genre": "Animation",
        "rating": 4,
        "watched": False
    }
]

import random
from unwatched_movies import get_unwatched_movies

def recommend_random_movie(movies):
    unwatched_movies = get_unwatched_movies(movies)

    if not unwatched_movies:
        return
    
    recommendation = random.choice(unwatched_movies) 
    print(recommendation)

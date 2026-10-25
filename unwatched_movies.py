
### User Story
# As a user, I want to display all movies I have not watched yet so that I can easily find something new to watch.

### Acceptance Criteria
# Only unwatched movies are displayed.
# Each movie displays its title, genre, and rating.
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
        "watched": True
    },
{
        "ID": 3,
        "title": "Frozen",
        "genre": "Animation",
        "rating": 4,
        "watched": False
    }
]


def get_unwatched_movies(movies):
    unwatched_movies = []

    for movie in movies:
        if not movie["watched"]:
            unwatched_movies.append(movie)

    return unwatched_movies

result = get_unwatched_movies(sample_library)
print(result)


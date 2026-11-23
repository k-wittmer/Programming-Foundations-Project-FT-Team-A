
### User Story
# As a user, I want to search for movies by title, genre, or rating so that I can quickly find movies matching my preferences.

### Acceptance Criteria
# Users can search by title.
# Users can search by genre.
# Users can search by rating.
# All matching movies are displayed.
# Title searches are case-insensitive.
# Genre searches are case-insensitive.
# A message is displayed if no matching movies are found.

import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"

import movies

movie_library = movies.load_movie_library()

def search_by_genre(movies, genre):
    results = []

    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            results.append(movie)

    return results

selected_genre = input("Enter a genre: ")
results = search_by_genre(movie_library, selected_genre)

if not results:
    print("No movies in selected genre")
else:
    for movie in results:
        print(
                    f'Title: {movie["title"]} | '
                    f'Genre: {movie["genre"]} | '
                    f'Rating: {movie["rating"]}')

def search_by_rating(movies, rating):
    results = []

    for movie in movies:
        if movie["rating"] == rating:
            results.append(movie)
    
    return results

selected_rating = int(input("Enter a rating: "))
results = search_by_rating(movie_library, selected_rating)

if not results:
    print("No movies in selected rating")
else:
    for movie in results:
        print(
                    f'Title: {movie["title"]} | '
                    f'Genre: {movie["genre"]} | '
                    f'Rating: {movie["rating"]}')

def search_by_title(movies, title):
    results = []

    for movie in movies:
        if title.lower() in movie["title"].lower():
            results.append(movie)
    return results

selected_title = input("Enter a title: ")
results = search_by_title(movie_library, selected_title)

if not results:
    print("No movies in selected title")
else:
   for movie in results:
           print(
                    f'Title: {movie["title"]} | '
                    f'Genre: {movie["genre"]} | '
                    f'Rating: {movie["rating"]}') 
# Add and edit movies.
import ui

import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"


#Gets the user input about the movie title.
def add_movie_title():
    movie_title = input("Name of the Movie: ").upper()

    return movie_title


#Gets the user input about the genre, which is to be assigned to the movie.
def add_movie_genre():
    selected_movie_genre = ui.movie_genres()
    movie_genre = ui.dict_movie_genre[selected_movie_genre]
   
    return movie_genre
    

#Gets the user input about the rating of the movie.
def add_movie_rating():
    movie_rating = int(input("How would you rate the movie from 1-5? (0 - to enter no rating): "))
    while 0 > movie_rating > 5:
        print("Invalid input. Rating must be between 1-5.")
        movie_rating = int(input("How would you rate the movie from 1-5? (Press Enter to add no rating): "))

    if movie_rating == 0:
        movie_rating = "**Not rated**"
        return movie_rating

    else:
        return movie_rating


#Gets the user input, if the movie is watched or not.
def add_movie_watched():
    watched = input("Did you already watch the movie? (y/n): ").lower().strip()
    while watched not in ("y", "n"):
        print("Invalid input. Please enter y or n.")
        watched = input("Did you already watch the movie? (y/n): ").lower().strip()
    if watched == "y":
        is_watched = True
    else:
        is_watched = False
    
    return is_watched


#Loads the movies.json into python.
def load_movie_library():
    if not FILE.exists():
        return []
    with open(FILE, "r", encoding = "utf-8") as file:
        return json.load(file)


#Saves the updates made to the movie list/dictionary.
def save_movies(movies):
    with open(FILE, "w", encoding = "utf-8") as file:
        json.dump(movies, file, indent = 4, ensure_ascii = False)


#Gets the next biggest ID to append to the list.
def next_id(movies):
    return max((m["ID"] for m in movies), default = 0) +1


#Add a movie to the movies.json file
def add_movie():
    print("Please add the following movie details:")
    title = add_movie_title()
    genre = add_movie_genre()
    rating = add_movie_rating()
    is_watched = add_movie_watched()

    movies = load_movie_library()
    movies.append({
        "ID": next_id(movies),
        "title": title,
        "genre": genre,
        "rating": rating,
        "watched": is_watched,
    })

    try:
        save_movies(movies)

    except Exception as error:
        print(f"Error, unable to save the movie to the library. {error}")
        return False

    return True






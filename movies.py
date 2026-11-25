# Add and edit movies.
import ui

import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"


#Gets the user input about the movie title.
def add_movie_title():
    while True:
        movie_title = input("Name of the Movie: ").upper()
        if not movie_title or movie_title.isspace():
            print("\n" + "=" * 60)
            print("Movie title cannot be empty.")
            print("=" * 60 + "\n\n")  
        else:
            break

    return movie_title


#Gets the user input about the genre, which is to be assigned to the movie.
def add_movie_genre():
    selected_movie_genre = ui.movie_genres()
    movie_genre = ui.dict_movie_genre[selected_movie_genre]
   
    return movie_genre
    

#Gets the user input about the rating of the movie.
def add_movie_rating():
    while True:
        movie_rating = (input("How would you rate the movie from 1-5? (0 - to enter no rating): ")).strip()
        try:
            movie_rating = int(movie_rating)
        except ValueError:
            print("Invalid input. The rating has to be in the range from 1-5? (0 - to enter no rating).")
        else:
            if movie_rating in range(0,6):
                break
            else:
                print("Invalid input. The rating has to be in the range from 1-5? (0 - to enter no rating).")

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
def save_movie_library(movie_library):
    try:
        with open(FILE, "w", encoding = "utf-8") as file:
            json.dump(movie_library, file, indent = 4, ensure_ascii = False)

    except Exception as error:
        print(f"Error, unable to save the movie library. {error}")
        is_success = False

    is_success = True

    if is_success:
        print("\n" + "=" * 60)
        print("Movie library saved successfully!")
        print("=" * 60 + "\n\n")  
        
    else:
        print("\n" + "=" * 60)
        print("Unable to save the movie library.")
        print("=" * 60 + "\n\n")  


#Gets the next biggest ID to append to the list.
def next_id(movie_library):
    return max((m["ID"] for m in movie_library), default = 0) +1


#Add a movie to the movies.json file
def add_movie():
    print("Please add the following movie details:")
    title = add_movie_title()
    genre = add_movie_genre()
    rating = add_movie_rating()
    is_watched = add_movie_watched()

    movie_library = load_movie_library()
    movie_library.append({
        "ID": next_id(movie_library),
        "title": title,
        "genre": genre,
        "rating": rating,
        "watched": is_watched,
    })

    return movie_library


def select_movie():
    movie_library = load_movie_library()

    if not movie_library:
        print("Your movie library is empty")
        return movie_library, None

    for movie in movie_library:
        ui.display_movie(movie)

    while True:
        try:
            selected_id = int(input("Choose a movie ID: ").strip())
        except ValueError:
            print("Please enter a whole number.")
            continue

        for movie in movie_library:
            if movie["ID"] == selected_id:
                return movie_library, movie

        print("Invalid movie ID. Please try again.")

def delete_movie():
    movie_library, movie = select_movie()

    if movie is None:
        return

    movie_library.remove(movie)
    save_movie_library(movie_library)

    print("Movie deleted:")
    ui.display_movie(movie)


# Ryan: edit the title or genre of a selected movie.
def edit_movie():
    movie_library, movie = select_movie()

    if movie is None:
        return

    choice = input("Change 1 - Title or 2 - Genre: ").strip()

    while choice not in ("1", "2"):
        print("Please enter 1 or 2.")
        choice = input("Change 1 - Title or 2 - Genre: ").strip()

    if choice == "1":
        title = input("New title: ").strip()

        while title == "":
            print("The title cannot be empty.")
            title = input("New title: ").strip()

        movie["title"] = title
    else:
        movie["genre"] = add_movie_genre()

    save_movie_library(movie_library)
    print("Movie updated:")
    ui.display_movie(movie)




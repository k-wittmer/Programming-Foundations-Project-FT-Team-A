#Program starting

import ui
import movies
import recommendations

import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"

#Marks the programm as running.
is_running = True

#Calls the main menu, where the user can initiate the desired action.
while is_running:
    user_operation = ui.main_menu()

    if user_operation == 1: #Function to add a movie.
        movie_library = movies.add_movie()
        movies.save_movie_library(movie_library)


    elif user_operation == 2: #Function to add/change a category.
        movie_library, selected_movie = movies.select_movie()
        new_genre = movies.add_movie_genre()

        for movie in movie_library:
            if movie["ID"] == selected_movie["ID"]:
                movie["genre"] = new_genre

        movies.save_movie_library(movie_library)


    elif user_operation == 3: #Calls the add/change rating feature.
        xxx

    elif user_operation == 4: #Calls the add/change watched status feature.
        xxx

    elif user_operation == 5: #xxx
        xxx

    elif user_operation == 6:
        movies.delete_movie()

    elif user_operation == 7: #xxx
        xxx

    elif user_operation == 8: #xxx
        xxx

    elif user_operation == 9: #xxx
        xxx

    elif user_operation == 10: #xxx
        xxx

    elif user_operation == 11: # Calls the genre suggestion feature.
        recommendations.genre_suggestion()

    elif user_operation == 12: #xxx
        xxx

    elif user_operation == 0: #Exits the programm.
        is_running = False
        print("Exiting the programm. Byeeee!")

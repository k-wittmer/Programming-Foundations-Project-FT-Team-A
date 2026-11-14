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


    if user_operation == 1: #Calls the add movie feature.
        is_success = movies.add_movie()
        if is_success:
            print("Movie added successfully!")
        else:
            print("Unable to add the movie to the library.")

    elif user_operation == 2: #Calls the add/change category feature.
        xxx

    elif user_operation == 3: #Calls the add/change rating feature.
        xxx

    elif user_operation == 4: #Calls the add/change watched status feature.
        xxx

    elif user_operation == 5: #xxx
        xxx

    elif user_operation == 6: #xxx
        xxx

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

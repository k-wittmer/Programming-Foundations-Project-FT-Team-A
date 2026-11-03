#Program starting

import ui
import movies
import recommendations

import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"


#Calls the main menu, where the user can initiate the desired action.
user_operation = ui.main_menu()


if user_operation == 1: #Calls the add movie feature.
    is_success = movies.add_movie()
    if is_success:
        print("Movie added successfully!")
    else:
        print("Unable to add the movie to the library.")
elif user_operation == 11:
    recommendations.genre_suggestion()
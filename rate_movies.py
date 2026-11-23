
### User Story
# As a user, I want to rate movies so that I can document my preferences.

### Acceptance Criteria
# [ ] Users can select an existing movie to rate.
# [ ] Ratings must be between 1 and 5.
# [ ] Ratings are saved and displayed with the movie.
# [ ] Existing ratings can be changed.
# [ ] Invalid selections or ratings display an error message.
# [ ] Invalid operations do not modify stored data.

import json
from pathlib import Path

#Sets/anchors the file path of the movies.json to the script, instead of the local directory.
FILE = Path(__file__).parent / "data" / "movies.json"

import movies

movie_library, selected_movie = movies.select_movie()

new_rating = movies.add_movie_rating()

def rate_movie():

    for movie in movie_library:
        if movie["ID"] == selected_movie["ID"]:
            movie["rating"] = new_rating
            break

     #save changes to json
    try:
        movies.save_movies(movie_library)
        print("Changes saved succesfully")
    except Exception as error:
        print(f"An error occured while trying to make changes: {error}")


#testing the function
if __name__ == "__main__":
    rate_movie()
    
    
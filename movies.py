# Add and edit movies.
import ui
import movies

#Add a Movie
def add_movie(): #Currently produces a Name Error, because it sais that "add_movie_title" is not defined. BUT IT IS!!!
    print("Please add the following movie details:")
    title = add_movie_title()
    genre = add_movie_genre()
    rating = add_movie_rating()
    is_watched = add_movie_watched()

    #Add the code to add the entries to the .json file. Also check for the next ID number.
    #ID": 1, "title": "Inception", "genre": "Science Fiction", "rating": 5, "watched": true

    return title, genre, rating, is_watched

test = add_movie()
print(test)


def add_movie_title():
    movie_title = input("Name of the Movie: ").upper()
    return movie_title


def add_movie_genre():
    import ui
    selected_movie_genre = ui.movie_genres()
    movie_genre = ui.dict_movie_genre[selected_movie_genre]
   
    return movie_genre
    

def add_movie_rating():
    movie_rating = int(input("How would you rate the movie from 1-5? (Press Enter to add no rating): "))
    while 1 > movie_rating > 5:
        print("Invalid input. Rating must be between 1-5.")
        movie_rating = int(input("How would you rate the movie from 1-5? (Press Enter to add no rating): "))
    
    return movie_rating


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


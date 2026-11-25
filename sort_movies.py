# Ryan: sort the library by title, genre or rating.
import movies
import ui


def title_key(movie):
    return movie["title"].lower()


def genre_key(movie):
    return movie["genre"].lower()


def rating_key(movie):
    rating = movie["rating"]

    if isinstance(rating, int):
        return rating

    return 0


def sort_movies():
    movie_library = movies.load_movie_library()

    if not movie_library:
        print("Your movie library is empty")
        return

    print("1 - Title A-Z")
    print("2 - Genre A-Z")
    print("3 - Rating highest first")

    choice = input("Choose a sort order: ").strip()

    while choice not in ("1", "2", "3"):
        print("Please enter 1, 2 or 3.")
        choice = input("Choose a sort order: ").strip()

    if choice == "1":
        result = sorted(movie_library, key=title_key)
    elif choice == "2":
        result = sorted(movie_library, key=genre_key)
    else:
        result = sorted(movie_library, key=rating_key, reverse=True)

    for movie in result:
        # Use a copy to format missing ratings only for the display.
        movie_to_display = movie.copy()
        if rating_key(movie) == 0:
            movie_to_display["rating"] = "Not rated"
        ui.display_movie(movie_to_display)

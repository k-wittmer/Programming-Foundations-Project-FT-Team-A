#Console input and outputs


# Main menu
def main_menu():
    print("==================================================")
    print("Select the number of the operation that you want to do.")
    print("")
    print("1 - Add Movie")
    print("2 - Categorize Movie")
    print("3 - Rate Movie")
    print("4 - Mark Movie as Watched")
    print("5 - Edit Movie")
    print("6 - Delete Movie")
    print("7 - Display Library")
    print("8 - Search Movies")
    print("9 - Sort Movies")
    print("10 - Random Recommendation")
    print("11 - Genre Suggestions")
    print("12 - Show Unwatched Movies")
    print("")
    print("0 - Exit")
    print("==================================================")

    while True:
        user_operation = input("Enter the number of the operation that you want to do: ").strip()
        try:
            user_operation = int(user_operation)
        except ValueError:
            print("Invalid input. Please enter the number of the operation that you want to do.")
        else:
            if user_operation in range(0,13):
                break
            else:
                print("Invalid input. Please enter the number of the operation that you want to do.")

    return user_operation


#List of movie genres
def movie_genres():
    print("==================================================")
    print("Select the movie genre.")
    print("")
    print("1 - Action")
    print("2 - Adventure")
    print("3 - Animation")
    print("4 - Comedy")
    print("5 - Crime")
    print("6 - Drama")
    print("7 - Documentary")
    print("8 - Fantasy")
    print("9 - Historical")
    print("10 - Horror")
    print("11 - Musical")
    print("12 - Mystery")
    print("13 - Romance")
    print("14 - Science-Fiction")
    print("15 - Thriller")
    print("16 - War")
    print("17 - Western")
    print("")
    print("==================================================")

    while True:
        movie_genre = input("Enter the number of the movie genre: ").strip()
        try:
            movie_genre = int(movie_genre)
        except ValueError:
            print("Invalid input. Please enter the number of the movie genre.")
        else:
            if movie_genre in range(1,18):
                break
            else:
                print("Invalid input. Please enter the number of the movie genre.")

    return movie_genre

#Dictionary of Movie Genres
dict_movie_genre = {1: "Action", 2: "Adventure", 3: "Animation", 4: "Comedy", 5: "Crime", 6: "Drama", 7: "Documentary", 8: "Fantasy", 9: "Historical", 10: "Horror", 11: "Musical", 12: "Mystery", 13: "Romance", 14: "Science-Fiction", 15: "Thriller", 16: "War", 17: "Western"}
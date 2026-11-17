
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


from unwatched_movies import sample_library

def search_by_genre(movies, genre):
    results = []

    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            results.append(movie)

    return results

selected_genre = input("Enter a genre: ")
results = search_by_genre(sample_library, selected_genre)

if not results:
    print("No movies in selected genre")
else:
    for movie in results:
        print(
                       f'Title: {movie["title"]} | '
                       f'Genre: {movie["genre"]} | '
                       f'Rating: {movie["rating"]}')
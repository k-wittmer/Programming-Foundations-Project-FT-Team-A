# Programming-Foundations-Project-FT-Team-A
# Creating a movie library 📽️

## Problem Description
It can be difficult to keep track of movies we want to watch,
which ones we have already seen and how much we liked them.
Our application addresses this problem by providing a simple command-line movie library where users can manage their collection and find a movie to watch.

For each movie, the application stores:
- **Title:** the name of the movie.
- **Genre:** the movie's category, such as comedy or action.
- **Rating:** an optional personal rating; otherwise displayed as "Not rated".
- **Watched status:** whether the movie has been watched or not.

## USER STORIES
As a user
I want to add movies to the library,
So that I can watch them later.
-> Responsibility: Kiran

As a user,
I want to be able to categorize the movies by genre,
So that I can search for them by genre.
-> Responsibility: Kiran

As a user,
I want to be able to rate the movies,
So that I can document my preferences.
-> Responsibility: Francisco

As a user,
I want to be able to mark a movie as watched,
So that I can see, which movies I already watched.
-> Responsibility: Francisco


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
As a user,
I want to be able to delete movies,
So that I can clean up my library.

  Acceptance criteria:
  - The user can select an existing movie to delete.
  - The selected movie is removed from the library; all other movies remain unchanged.
  - A confirmation message is displayed after successful deletion.
  - If the library is empty or the selection is invalid, a message is displayed and nothing is deleted.
    
  -> Responsibility: Ryan
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Searching/Sorting/Display
As a user,
I want to be able to display my whole movie library, 
So that I can see all my movies in the library.
-> Responsibility: Francisco

As a user,
I want to be able to search for movies by title, genre and rating,
So that I can quickly find movies matching my preferences.
-> Responsibility: Max
Acceptance criteria: User can search by title, genre or rating -> all matching movies are displayed -> title and genre searches are case-insensitive -> if no matching movies are found, display a message 


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
As a user,
I want to be able to sort the movies by genre, name and rating,
So that I can search for them by name, genre, rating.

  Acceptance criteria:
  - The user can choose one of three sort orders: title alphabetically (A–Z), genre alphabetically (A–Z), or rating from highest to lowest.
  - Movies without a rating appear last when sorting by rating.
  - The sorted list displays each movie's title, genre, rating and watched status. Missing ratings are displayed as "Not rated".
  - Sorting changes only the display order, not the movie details.
  - If the library is empty, the application displays "Your movie library is empty".
    
  -> Responsibility: Ryan
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
As a user,
I want to edit the title or genre of an existing movie so that I can correct mistakes without deleting and adding the movie again.

  Acceptance criteria:
  - The user can select an existing movie and choose whether to edit its title or genre.
  - After a valid change, the updated value is shown when the library is displayed.
  - Empty or whitespace-only values are rejected with an error message, and the existing value remains unchanged.
  - Editing the title or genre leaves the movie's rating and watched status unchanged.
  - If the library is empty or the selection is invalid, a message is displayed and no movie is changed.
    
  -> Responsibility: Ryan
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


As a user,
I want receive a random movie recommendation from my movie library,
So that I can decide what to watch without searching for one manually.
-> Responsibility: Max
Acceptance criteria: The application randomly selects one movie from Not Watched- library -> recommended movie's title and genre are displayed to the user -> if no unwatched movies exist in Not Watched- library, a message is displayed to user

As a user,
I want to get a movie suggestion by a genre that I provide,
So that I don’t have to search the library myself.
-> Responsibility: Kiran

As a user,
I want to be able to display all the movies I haven’t watched yet,
So that I can easily find a movie I haven’t watched yet.
-> Responsibility: Max
Acceptance criteria: Only movies in Not Watched- library are displayed -> all displayed movies have their title, genre and rating visible to user -> if no movies are found in Not Watched- library, a message is displayed to user

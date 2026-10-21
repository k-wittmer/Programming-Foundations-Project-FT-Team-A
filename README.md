
# 🎬 Movie Library
### Programming Foundations Project | FT – Team A

A simple Python command-line application to organize, manage, and discover movies.

---

## 📖 About the Project

Keeping track of movies we want to watch, movies we have already seen, and how much we liked them can be difficult.

**Movie Library** solves this problem by providing a simple command-line application that allows users to manage their personal movie collection.

Users can add, edit, delete, search, sort, and rate movies, track their watched status, and receive movie recommendations.

### 🎯 Project Goals

- Build a functional movie management application using Python.
- Apply fundamental programming concepts.
- Practice collaborative software development using GitHub.
- Create an intuitive command-line user experience.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ➕ Add Movies | Add new movies to the library |
| 🏷️ Categorize | Assign and modify movie genres |
| ⭐ Rate Movies | Rate movies from 1 to 5 |
| ✅ Watched Status | Mark movies as watched or unwatched |
| 🗑️ Delete Movies | Remove movies from the library |
| 📋 Display Library | View all stored movies |
| 🔍 Search Movies | Search by title, genre, or rating |
| 🔃 Sort Movies | Sort by title, genre, or rating |
| ✏️ Edit Movies | Update movie titles and genres |
| 🎲 Random Movie | Get a random unwatched movie |
| 🎯 Genre Suggestion | Get random suggestions by genre |
| 🍿 Watchlist | Display all unwatched movies |

---

## 🗂️ Movie Data Structure

Each movie contains the following information:

| Attribute | Description | Example |
|-----------|-------------|---------|
| Title | Name of the movie | Interstellar |
| Genre | Movie category | Sci-Fi |
| Rating | Personal rating (1–5) | 5 |
| Watched | Whether the movie was watched | True |

Movies without a rating are displayed as **"Not rated"**.

---

## 👥 Team & Responsibilities

| Team Member | Responsibilities |
|-------------|------------------|
| **Kiran** | Add Movies, Categorize Movies, Genre Suggestions |
| **Francisco** | Rate Movies, Watched Status, Display Library |
| **Ryan** | Delete Movies, Sort Movies, Edit Movies |
| **Max** | Search Movies, Random Recommendations, Watchlist |

---

# 📋 User Stories & Acceptance Criteria

## 1. ➕ Add Movies
**Responsible:** Kiran

### User Story
> As a user, I want to add movies to the library so that I can watch them later.

### Acceptance Criteria
- [ ] Users can add a movie to the library.
- [ ] The program guides users through the process.
- [ ] A confirmation message is displayed after successful addition.

---

## 2. 🏷️ Categorize Movies
**Responsible:** Kiran

### User Story
> As a user, I want to categorize movies by genre so that I can search for them by genre.

### Acceptance Criteria
- [ ] Users can assign a genre to a movie.
- [ ] Users can change a genre if an incorrect one was assigned.

---

## 3. ⭐ Rate Movies
**Responsible:** Francisco

### User Story
> As a user, I want to rate movies so that I can document my preferences.

### Acceptance Criteria
- [ ] Users can select an existing movie to rate.
- [ ] Ratings must be between 1 and 5.
- [ ] Ratings are saved and displayed with the movie.
- [ ] Existing ratings can be changed.
- [ ] Invalid selections or ratings display an error message.
- [ ] Invalid operations do not modify stored data.

---

## 4. ✅ Mark Movies as Watched
**Responsible:** Francisco

### User Story
> As a user, I want to mark movies as watched so that I can see which movies I have already watched.

### Acceptance Criteria
- [ ] Users can select an existing movie.
- [ ] Selected movies can be marked as watched.
- [ ] Other movies remain unchanged.
- [ ] Watched status is saved and displayed.
- [ ] Movies can be marked as unwatched again.
- [ ] Invalid selections display an error without changing data.

---

## 5. 🗑️ Delete Movies
**Responsible:** Ryan

### User Story
> As a user, I want to delete movies so that I can clean up my library.

### Acceptance Criteria
- [ ] Users can select an existing movie to delete.
- [ ] Only the selected movie is removed.
- [ ] Other movies remain unchanged.
- [ ] Successful deletion displays a confirmation message.
- [ ] Empty libraries or invalid selections display an error.
- [ ] Invalid operations do not delete any movies.

---

## 6. 📋 Display Movie Library
**Responsible:** Francisco

### User Story
> As a user, I want to display my entire movie library so that I can see all my movies.

### Acceptance Criteria
- [ ] Users can display the entire library.
- [ ] All stored movies are displayed.
- [ ] Each movie shows its title, genre, rating, and watched status.
- [ ] Displaying movies does not modify stored data.
- [ ] An empty library displays an appropriate message.

---

## 7. 🔍 Search Movies
**Responsible:** Max

### User Story
> As a user, I want to search for movies by title, genre, or rating so that I can quickly find movies matching my preferences.

### Acceptance Criteria
- [ ] Users can search by title.
- [ ] Users can search by genre.
- [ ] Users can search by rating.
- [ ] All matching movies are displayed.
- [ ] Title searches are case-insensitive.
- [ ] Genre searches are case-insensitive.
- [ ] A message is displayed if no matching movies are found.

---

## 8. 🔃 Sort Movies
**Responsible:** Ryan

### User Story
> As a user, I want to sort movies by title, genre, or rating so that I can organize and find movies more easily.

### Acceptance Criteria
- [ ] Users can sort titles alphabetically (A–Z).
- [ ] Users can sort genres alphabetically (A–Z).
- [ ] Users can sort ratings from highest to lowest.
- [ ] Movies without ratings appear last when sorting by rating.
- [ ] Sorted results show title, genre, rating, and watched status.
- [ ] Missing ratings are displayed as "Not rated".
- [ ] Sorting does not modify movie details.
- [ ] Empty libraries display "Your movie library is empty".

---

## 9. ✏️ Edit Movies
**Responsible:** Ryan

### User Story
> As a user, I want to edit a movie's title or genre so that I can correct mistakes without deleting and re-adding the movie.

### Acceptance Criteria
- [ ] Users can select an existing movie.
- [ ] Users can edit the title or genre.
- [ ] Valid changes are reflected in the library.
- [ ] Empty or whitespace-only values are rejected.
- [ ] Invalid changes preserve the existing values.
- [ ] Ratings and watched status remain unchanged.
- [ ] Invalid selections display an error message.
- [ ] An empty library cannot be edited.

---

## 10. 🎲 Random Movie Recommendation
**Responsible:** Max

### User Story
> As a user, I want to receive a random movie recommendation from my library so that I can decide what to watch without searching manually.

### Acceptance Criteria
- [ ] The program randomly selects an unwatched movie.
- [ ] The recommended movie's title and genre are displayed.
- [ ] Only unwatched movies are eligible.
- [ ] A message is displayed if no unwatched movies are available.

---

## 11. 🎯 Movie Suggestions by Genre
**Responsible:** Kiran

### User Story
> As a user, I want to receive movie suggestions based on a genre I provide so that I do not have to search the library manually.

### Acceptance Criteria
- [ ] Users can request movie suggestions by genre.
- [ ] The program selects three random movies from the chosen genre.
- [ ] The selected movies are displayed to the user.

---

## 12. 🍿 Display Unwatched Movies
**Responsible:** Max

### User Story
> As a user, I want to display all movies I have not watched yet so that I can easily find something new to watch.

### Acceptance Criteria
- [ ] Only unwatched movies are displayed.
- [ ] Each movie displays its title, genre, and rating.
- [ ] A message is displayed if no unwatched movies are available.

---

## 💻 Example Interface

The following illustrates the planned command-line interface:

```text
========================================
           🎬 MOVIE LIBRARY
========================================

1. Add Movie
2. Categorize Movie
3. Rate Movie
4. Mark Movie as Watched
5. Delete Movie
6. Display Library
7. Search Movies
8. Sort Movies
9. Edit Movie
10. Random Recommendation
11. Genre Suggestions
12. Show Unwatched Movies

0. Exit

========================================
Enter your choice:
```

---

## 📈 Development Progress

| Feature | Assigned To | Status |
|---------|-------------|--------|
| Add Movies | Kiran | ⬜ Planned |
| Categorize Movies | Kiran | ⬜ Planned |
| Rate Movies | Francisco | ⬜ Planned |
| Watched Status | Francisco | ⬜ Planned |
| Delete Movies | Ryan | ⬜ Planned |
| Display Library | Francisco | ⬜ Planned |
| Search Movies | Max | ⬜ Planned |
| Sort Movies | Ryan | ⬜ Planned |
| Edit Movies | Ryan | ⬜ Planned |
| Random Recommendation | Max | ⬜ Planned |
| Genre Suggestions | Kiran | ⬜ Planned |
| Display Unwatched Movies | Max | ⬜ Planned |

---

## 🎓 Academic Project

**Course:** Programming Foundations

**Project:** Creating a Movie Library

**Team:** FT – Team A

This project was developed as part of the Programming Foundations course to demonstrate fundamental Python programming skills and collaborative software development.

---

<p align="center">
  <strong>🎬 Movie Library — FT Team A</strong>
</p>

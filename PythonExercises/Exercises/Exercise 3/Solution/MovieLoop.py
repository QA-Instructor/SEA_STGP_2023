movies = ["Jaws", "Star Wars", "Vanilla Sky", "The Mission", "Bridget Jones Diary 2"]

# Iterate through each movie and print out
for movieTitle in movies:
    print(movieTitle)

# Display an indexed list of movies and length of movie names.
for idx, movieTitle in enumerate(movies, start=1):
    print(idx + "." + movieTitle + ", " + len(movieTitle))



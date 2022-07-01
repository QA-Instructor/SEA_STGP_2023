movies = ["Jaws", "Star Wars", "Vanilla Sky", "The Mission", "Bridget Jones Diary 2"]
print(movies)
new_movie = input("Enter Movie Title to Add: ")
if len(movies) > 0:
    print(len(movies), "movies in list")
else:
    print("Empty list")


# Check if movie exists if it doesn't then append to array, otherwise say it exists
if new_movie in movies:
    print("Movie exists!")
else:
    movies.append(new_movie)
    print(movies)

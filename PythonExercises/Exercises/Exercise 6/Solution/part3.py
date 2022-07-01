import imdb
import re

ia = imdb.IMDb()

pattern = input("Enter movie name: ")

for rank, movie in enumerate(ia.get_top250_movies(), start=1):
    m = re.search(pattern, str(movie), re.IGNORECASE)
    if m:
        print(f"{rank:>4d}: {movie}")


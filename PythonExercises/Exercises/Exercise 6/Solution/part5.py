import imdb
import re
ia = imdb.IMDb()

count = 0
pattern1 = r"^the"
pattern2 = r"\d"
pattern3 = r"[aeiou]{3}"
pattern4 = r"^(.).*\1$"
pattern5 = r"^[^a-z]+$"
pattern6 = r"\s+(\w+)\s+.*\s+\1\s+"

for rank, movie in enumerate(ia.get_top250_movies(), start=1):
    # Swap pattern below to any of the above string objects.
    m = re.search(pattern6, str(movie), re.IGNORECASE)
    if m:
        print(f"{rank:>4d}: {movie}")
        count += 1

print(f"Total lines = {count}")



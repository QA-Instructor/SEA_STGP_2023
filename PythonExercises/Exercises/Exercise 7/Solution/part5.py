movies = [{"title": "Jaws", "director": "Steven Spielberg", "year": "1975"},
          {"title": "Star Wars", "director": "Steven Spielberg", "year": "1977"}, {"title": "Vanilla Sky", "director": "Cameron Crowe", "year": "2001"},
          {"title": "The Mission", "director": "Rolan Joffe", "year": "1986"},
          {"title": "Bridget Jones Diary", "director": "Sharron McGuire", "year": "2001"}
]

# Open file handle for writing in text mode.
fh_out = open(r"C:\labs\mymovies.txt", mode="wt")

# Iterate through each movie and print out title
for movie in movies:
    # The following print parameters span multiple lines.
    print(f"{movie['year']:>10s} - "
          f"Title: {movie['title'].upper():<20s} "
          f"Director: {movie['director']:>20s}", file=fh_out)



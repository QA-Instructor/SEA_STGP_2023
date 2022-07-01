movies = [{"title": "Jaws", "director": "Steven Spielberg", "year": "1975"},
{"title": "Star Wars", "director": "Steven Spielberg", "year": "1977"},
{"title": "Vanilla Sky", "director": "Cameron Crowe", "year": "2001"},
{"title": "The Mission", "director": "Rolan Joffe", "year": "1986"},
{"title": "Bridget Jones Diary", "director": "Sharron McGuire", "year": "2001"}]

title = input("Enter Movie Title: ")

for movie in movies:
    if movie["title"] == title:
        print("Title:" + movie["title"])
        print("Director:" + movie["director"])
        print("Year:" + movie["year"])



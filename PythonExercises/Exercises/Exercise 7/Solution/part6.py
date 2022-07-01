import pprint
import gzip
import pickle

movies = [{"title": "Jaws", "director": "Steven Spielberg", "year": "1975"},
          {"title": "Star Wars", "director": "Steven Spielberg", "year": "1977"}, {"title": "Vanilla Sky", "director": "Cameron Crowe", "year": "2001"},
          {"title": "The Mission", "director": "Rolan Joffe", "year": "1986"},
          {"title": "Bridget Jones Diary", "director": "Sharron McGuire", "year": "2001"}
]

# Open compressed file handle for writing in binary mode.
fh_in = gzip.open(r"C:\labs\mymovies.pgz", mode="rb")
pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL)
fh_out.close()

# Open compressed file handle for reading in binary mode.
fh_in = gzip.open(r"C:\labs\mymovies.pgz", mode="rb")
films = pickle.load(fh_in)
fh_in.close()

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)




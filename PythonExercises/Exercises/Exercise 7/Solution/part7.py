import imdb

ia = imdb.IMDb()
fh_out = open(r"c:\labs\top250.txt", mode="wt")

for rank, movie in enumerate(ia.get_top250_movies(), start=1):
    print(f"{rank:>4d}: {movie}")
    print(f"{rank:>4d}: {movie}", file=fh_out)
fh_out.close()




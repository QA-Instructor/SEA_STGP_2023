movie = "Local Hero, 111 minutes, Bill Forsyth, Burt Lancaster"
print("-" * len(movie))
print(movie.replace(",", ":"))
print(f"{'Film':>15s}: {movie[0:10].upper():<10s}")
print(f"{'Duration':>15s}: {movie[12:23]:<10s}")
print(f"{'Director':>15s}: {movie[25:37]:<10s}")
print(f"{'Starring':>15s}: {movie[39:]:<10s}")
print("-" * len(movie))


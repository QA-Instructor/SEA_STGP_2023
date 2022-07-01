movie = "Local Hero, 111 minutes, Bill Forsyth, Burt Lancaster"
fields = movie.split(",")

hours = int(fields[1].split()[0]) // 60
mins =  int(fields[1].split()[0]) % 60

print("-" * len(movie))
print(movie.replace(",", ":"))
print("Film: " + fields[0])
print("Duration: " + str(hours) + " hour, " + str(mins) + " mins")
print("Director: " + fields[2])
print("Starring: " + fields[3])
print("-" * len(movie))


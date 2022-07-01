#! /usr/bin/python

import imdb

ia = imdb.IMDb()

for movie in ia.get_top250_movies():
    print(movie)

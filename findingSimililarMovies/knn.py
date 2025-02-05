import operator
import pandas as pd
import numpy as np
from scipy import spatial


r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./findingSimililarMovies/data/u.data',
                      sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

movieProperties = ratings.groupby('movie_id').agg(
    {'rating': [np.size, np.mean]})

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
normalizedNumRatings = movieNumRatings.apply(
    lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

movieDict = {}

with open('./findingSimililarMovies/data/u.item', encoding='ISO-8859-1') as f:
    temp = ''
    for line in f:
        # line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), normalizedNumRatings.loc[movieID].get(
            'size'), movieProperties.loc[movieID].rating.get('mean'))


def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance


def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors


K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print(movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))

avgRating /= K

print(avgRating)

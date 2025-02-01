import numpy as np
import pandas as pd
import os

print(os.getcwd())

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./findingSimililarMovies/data/u.data',
                      sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('./findingSimililarMovies/data/u.item',
                     sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)


movieRatings = ratings.pivot_table(index=['user_id'], columns=[
                                   'title'], values='rating')

starWarsRatings = movieRatings['Star Wars (1977)']

similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()

df = pd.DataFrame(similarMovies)


movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
print(movieStats.head())

popularMovies = movieStats['rating']['size'] >=100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

mappedColumnsMoviestat=movieStats[popularMovies]
mappedColumnsMoviestat.columns=[f'{i}|{j}' if j != '' else f'{i}' for i,j in mappedColumnsMoviestat.columns]
df = mappedColumnsMoviestat.join(pd.DataFrame(similarMovies, columns=['similarity']))

print(df.sort_values(['similarity'], ascending=False)[:15])

import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./findingSimililarMovies/data/u.data',
                      sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('./findingSimililarMovies/data/u.item',
                     sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

userRatings = ratings.pivot_table(index=['user_id'], columns=[
                                  'title'], values=['rating'])

corr_matrix = userRatings.corr(method='pearson', min_periods=100)

myRatings = userRatings.loc[0].dropna()

simCandidated = pd.Series()

for i in range(0, len(myRatings.index)):
    sims = corr_matrix[myRatings.index[i]].dropna()
    sims = sims.map(lambda x: x * myRatings[i])
    simCandidated = pd.concat([simCandidated, sims])


simCandidated = simCandidated.groupby(simCandidated.index).sum()
simCandidated.sort_values(inplace=True, ascending=False)

filteredSims = simCandidated.drop(myRatings.index)
print(filteredSims.head())


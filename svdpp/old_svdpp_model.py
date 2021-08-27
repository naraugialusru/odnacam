'''
This model is based on model (15) in Factorization Meets the Neighborhood: a Multifaceted Collaborative Filtering Model
by Yehuda Koren (https://people.engr.tamu.edu/huangrh/Spring16/papers_course/matrix_factorization.pdf)

The paper MATRIX FACTORIZATION TECHNIQUES FOR RECOMMENDER SYSTEMS by Yehuda Koren, Robert Bell and Chris Volinsky
(https://www.inf.unibz.it/~ricci/ISR/papers/ieeecomputer.pdf) is a very clear read, and helpful for
the first paper. Model (4) in this paper is similar
'''

import numpy as np
import pandas as pd

gamma = 0.002
lam = 0.05


class SVDpp():
    def __init__(self, user_ratings_df, num_latent_features):
        self.users = user_ratings_df.index
        self.movies = user_ratings_df.columns
        self.r = {(u, i): user_ratings_df[i][u] for u in self.users for i in self.movies
                  if pd.notnull(user_ratings_df[i][u])}
        self.N = {u: {m for (v, m) in self.r.keys() if v == u} for u in self.users}
        ratings = [self.r.get(k) for k in self.r.keys()]
        self.mu = sum(ratings) / len(ratings)

        self.bu = np.zeros(len(self.users))
        self.bi = np.zeros(len(self.movies))
        self.qi = np.zeros((len(self.movies), num_latent_features))
        self.pu = np.zeros((len(self.users), num_latent_features))

        self.user_index = dict(zip(self.users, range(len(self.users))))
        self.movie_index = dict(zip(self.movies, range(len(self.movies))))

        self.index_user = dict(enumerate(self.users))
        self.index_movie = dict(enumerate(self.movies))

    def r_hat(self, u, i):
        ui = self.user_index[u]
        mi = self.movie_index[i]
        return self.mu + self.bu[ui] + self.bi[mi] + np.dot(self.qi[mi:][0], self.pu[ui:][0])

    def e(self, u, m):
        return self.r[u, m] - self.r_hat(u, m)

    def loss(self):
        tot_loss = 0
        for u, i in self.r.keys():
            tot_loss += (self.r[u, i] - self.r_hat(u, i)) ** 2
            ui = self.user_index[u]
            mi = self.movie_index[i]
            tot_loss += np.dot(self.qi[mi:][0], self.qi[mi:][0])
            tot_loss += np.dot(self.pu[ui:][0], self.pu[ui:][0])
            tot_loss += np.dot(self.bi, self.bi)
            tot_loss += np.dot(self.bu, self.bu)
        return tot_loss

    def gradient(self):
        # sum = np.zeros((len(self.users),))
        # for j in range(len(self.users)):
        #     for m in self.N[self.index_user[j]]:
        #         sum[j] += self.e(self.index_user[j], m)


        dbu = np.array([sum([self.e(self.index_user[j], i) for i in self.N[self.index_user[j]]]) for j in
                         range(len(self.users))]) - 2 * lam * self.bu
        # dbi = e(u, i) - 2 * lam * bi
        # dqi = np.dot(e(u, i), pu) - 2 * lam * qi
        # dpu = np.dot(e(u, i), qi) - 2 * lam * pu
        return dbu  # , dbi, dqi, dpu]


if __name__ == "__main__":
    import extract_load_transform

    urdf = extract_load_transform.get_user_ratings_dataframe(rows=10)
    svdpp = SVDpp(user_ratings_df=urdf, num_latent_features=5)

    usr, mve = list(svdpp.r.keys())[0]

    print(svdpp.r_hat(usr, mve))
    print(svdpp.e(usr, mve))
    print(svdpp.gradient())

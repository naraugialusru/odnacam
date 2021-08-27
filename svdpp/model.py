'''
This model is based on model (15) in Factorization Meets the Neighborhood: a Multifaceted Collaborative Filtering Model
by Yehuda Koren (https://people.engr.tamu.edu/huangrh/Spring16/papers_course/matrix_factorization.pdf)

The paper MATRIX FACTORIZATION TECHNIQUES FOR RECOMMENDER SYSTEMS by Yehuda Koren, Robert Bell and Chris Volinsky
(https://www.inf.unibz.it/~ricci/ISR/papers/ieeecomputer.pdf) is a very clear read, and helpful for
the first paper. Model (4) in this paper is similar
'''

import numpy as np


class SVDpp:
    def __init__(self, data, num_latent_features):
        self.users = data.users
        self.movies = data.movies
        self.num_latent_features = num_latent_features

        ratings = [data.ratings[u, m] for (u, m) in data.ratings.keys()]
        self.mu = sum(ratings) / len(ratings)

        # biases
        self.bu = {u: 0 for u in self.users}
        self.bm = {m: 0 for m in self.movies}
        # qualities and preferences
        self.qm = {m: np.random.rand(self.num_latent_features) for m in self.movies}
        self.pu = {u: np.random.rand(self.num_latent_features) for u in self.users}

    def __call__(self, u, m):
        return self.mu + self.bu[u] + self.bm[m] + np.dot(self.qm[m], self.pu[u])

    def parameters(self):
        return self.bu, self.bm, self.qm, self.pu


if __name__ == "__main__":
    import extract_load_transform
    import data_objects

    urdf = extract_load_transform.get_user_ratings_dataframe(rows=10)
    dta = data_objects.SVDppData(urdf)
    svdpp = SVDpp(data=dta, num_latent_features=5)

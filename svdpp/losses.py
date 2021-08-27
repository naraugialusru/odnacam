import numpy as np


def error(t, p):
    return t - p


class SVDppLoss:
    def __init__(self, lam=0.05):
        self.lam = lam

    def __call__(self, targ, pred):
        try:
            return sum([(t - p) ** 2 for t, p in zip(targ, pred)])
        except TypeError:
            return (targ - pred) ** 2

    def cost(self, targ, pred, parameters):
        return self.__call__(targ, pred) + self.lam * sum([v ** 2 for p in parameters for k, v in p])

    def gradient(self, users, movies, model, data):
        bu_array = np.array([model.bu[u] for u in users])
        bm_array = np.array([model.bm[m] for m in movies])
        qm_array = np.array([model.qm[m] for m in movies])
        pu_array = np.array([model.pu[u] for u in users])
        error_matrix = np.array([[data.ratings[u, m] - model(u, m) if (u, m) in data.ratings.keys() else 0
                                  for m in movies] for u in users])

        dbu_array = np.matmul(error_matrix, np.ones(len(movies))) - self.lam * bu_array
        dbm_array = np.matmul(np.ones(len(users)), error_matrix) - self.lam * bm_array
        dqm_array = np.matmul(error_matrix.transpose(), pu_array) - self.lam * qm_array
        dpu_array = np.matmul(error_matrix, qm_array) - self.lam * pu_array

        dbu = {users[i]: -dbu_array[i] for i in range(len(users))}
        dbm = {movies[i]: -dbm_array[i] for i in range(len(movies))}
        dqm = {movies[i]: -dqm_array[i] for i in range(len(movies))}
        dpu = {users[i]: -dpu_array[i] for i in range(len(users))}

        return dbu, dbm, dqm, dpu  # these can be used to step and then update the parameters in the model later.


if __name__ == "__main__":
    import extract_load_transform
    import data_objects
    import model

    urdf = extract_load_transform.get_user_ratings_dataframe(rows=10)
    dta = data_objects.SVDppData(urdf)
    svdpp = model.SVDpp(data=dta, num_latent_features=5)
    loss = SVDppLoss()
    targets = [dta.ratings[u, m] for u, m in dta.ratings.keys()]
    predictions = [svdpp(u, m) for u, m in dta.ratings.keys()]
    ls = loss(targets, predictions)
    grd = loss.gradient(svdpp.users, svdpp.movies, svdpp, dta)

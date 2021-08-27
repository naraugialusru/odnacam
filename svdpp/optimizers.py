import numpy as np


class SDVppStandardGD:
    def __init__(self, alpha=0.001):
        self.alpha = alpha

    def step(self, parameters, grad):
        out = []
        for p, g in zip(parameters, grad):
            out.append({k: p[k] - self.alpha * g[k] for k in g.keys()})
        return tuple(out)


class SDVppAdamOptim:
    def __init__(self, alpha=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.m = ({}, {}, {}, {})  # bu, bm, qm, pu
        self.v = ({}, {}, {}, {})
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.alpha = alpha
        self.step_nums = ({}, {}, {}, {})

    def step(self, parameters, grad):
        m_hat = []
        v_hat = []
        theta_out = []
        for s, mm, vv, p, g in zip(self.step_nums, self.m, self.v, parameters, grad):
            s.update({k: s.get(k, 0) + 1 for k in g.keys()})
            mm.update({k: self.beta1 * mm.get(k, 0) + (1 - self.beta1) * g[k] for k in g.keys()})
            vv.update({k: self.beta2 * vv.get(k, 0) + (1 - self.beta2) * g[k] ** 2 for k in g.keys()})
            m_hat.append({k: mm[k] / (1 - self.beta1 ** s[k]) for k in g.keys()})
            v_hat.append({k: vv[k] / (1 - self.beta2 ** s[k]) for k in g.keys()})
            theta_out.append({k: p[k] - self.alpha * (m_hat[-1][k] / (np.sqrt(v_hat[-1][k]) + self.epsilon))
                              for k in g.keys()})
        return tuple(theta_out)


if __name__ == "__main__":
    import extract_load_transform
    import data_objects
    import model
    import losses

    std_opt = SDVppStandardGD()
    adam_opt = SDVppAdamOptim()
    urdf = extract_load_transform.get_user_ratings_dataframe(rows=10)
    dta = data_objects.SVDppData(urdf)
    svdpp = model.SVDpp(data=dta, num_latent_features=5)
    loss = losses.SVDppLoss()
    grd = loss.gradient(svdpp.users, svdpp.movies, svdpp, dta)
    params = svdpp.parameters()
    std_step = std_opt.step(params, grd)
    adam_step = adam_opt.step(params, grd)

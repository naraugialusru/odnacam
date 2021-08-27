from functools import reduce
from operator import mul
import numpy as np
from optimizers import SDVppStandardGD


def svdpp_gradient_descent(model, loss, data, users=None, movies=None, optimizer=None, epochs=20):
    if optimizer is None:
        optimizer = SDVppStandardGD()
    if users is None:
        users = data.users
    if movies is None:
        movies = data.movies

    losses = []
    for epoch in range(epochs):
        grad = loss.gradient(users, movies, model, data)
        up = optimizer.step(parameters=model.parameters(), grad=grad)
        for p, upp in zip(model.parameters(), up):
            p.update(upp)
        if reduce(mul, [np.all(0 == g[k]) for g in grad for k in g.keys()], 1):
            print("Convergence!")
            break
        lss = sum([loss(data.ratings[u, m], model(u, m)) for (u, m) in data.ratings.keys()])
        losses.append(lss)
        print(f"Epoch = {epoch}: loss = {lss}")
    return losses


if __name__ == "__main__":
    import losses
    import model
    import extract_load_transform
    import data_objects
    import optimizers
    import matplotlib.pyplot as plt

    loss = losses.SVDppLoss()
    df = extract_load_transform.get_user_ratings_dataframe(rows=1000)
    data = data_objects.SVDppData(df)
    svdpp_std = model.SVDpp(data=data, num_latent_features=5)
    svdpp_adam = model.SVDpp(data=data, num_latent_features=5)

    std_opt = optimizers.SDVppStandardGD()
    adam_opt = optimizers.SDVppAdamOptim()
    epochs = 600

    print("Standard steps:")
    std_losses = svdpp_gradient_descent(svdpp_std, loss, data, optimizer=std_opt, epochs=epochs)
    print("")

    print("Adam steps:")
    adam_losses = svdpp_gradient_descent(svdpp_adam, loss, data, optimizer=adam_opt, epochs=epochs)

    plt.plot(range(epochs), std_losses[:epochs])
    plt.plot(range(epochs), adam_losses[:epochs])
    plt.legend(["std", "adam"])
    plt.show()
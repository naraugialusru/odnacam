import pandas as pd

class SVDppData:
    def __init__(self, df):
        self.users = df.index
        self.movies = df.columns
        self.ratings = {(u, m): df[m][u] for u in self.users for m in self.movies
                  if pd.notnull(df[m][u])}


if __name__ == "__main__":
    import extract_load_transform
    urdf = extract_load_transform.get_user_ratings_dataframe()
    data = SVDppData(urdf)

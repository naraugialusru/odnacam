import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi


def download_kaggle_files():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('netflix-inc/netflix-prize-data', path='/Users/pcc33/Downloads/',
                               unzip=True)


def truncated_readfile(file_path, rows=100000):
    data_dict = {'Cust_Id': [], 'Movie_Id': [], 'Rating': [], 'Date': []}
    with open(file_path, "r") as f:
        count = 0
        for line in f:
            count += 1
            if count > rows:
                break

            if ':' in line:
                movie_id = line[:-2]  # remove the last character ':'
                movie_id = int(movie_id)
            else:
                customer_id, rating, date = line.split(',')
                data_dict['Cust_Id'].append(customer_id)
                data_dict['Movie_Id'].append(movie_id)
                data_dict['Rating'].append(rating)
                data_dict['Date'].append(date.rstrip("\n"))

    return pd.DataFrame(data_dict)


def get_truncated_dataframe(rows=100000):
    rws = rows // 4
    df1 = truncated_readfile('/Users/pcc33/Downloads/combined_data_1.txt', rows=rws)
    df2 = truncated_readfile('/Users/pcc33/Downloads/combined_data_2.txt', rows=rws)
    df3 = truncated_readfile('/Users/pcc33/Downloads/combined_data_3.txt', rows=rws)
    df4 = truncated_readfile('/Users/pcc33/Downloads/combined_data_4.txt', rows=rows - 3 * rws)
    df1['Rating'] = df1['Rating'].astype(float)
    df2['Rating'] = df2['Rating'].astype(float)
    df3['Rating'] = df3['Rating'].astype(float)
    df4['Rating'] = df4['Rating'].astype(float)
    df = df1.copy()
    df = df.append(df2)
    df = df.append(df3)
    df = df.append(df4)
    return df


def get_user_ratings_dataframe(rows=100000):
    df = get_truncated_dataframe(rows=rows)
    user_ratings_df = df.pivot_table(index='Cust_Id', columns='Movie_Id', values='Rating', aggfunc='mean')
    return user_ratings_df


if __name__=="__main__":
    urdf = get_user_ratings_dataframe()

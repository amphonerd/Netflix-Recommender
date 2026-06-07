import pandas as pd

def get_data():
    df = pd.read_csv("data/netflix_titles.csv")

    df = df.fillna("")

    df["tags"] = (
        df["director"]
        + " "
        + df["cast"]
        + " "
        + df["listed_in"]
        + " "
        + df["description"]
    )

    return df
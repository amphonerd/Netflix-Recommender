from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def make_model(df):
    tfidf = TfidfVectorizer(stop_words="english")
    vectors = tfidf.fit_transform(df["tags"])
    sim = cosine_similarity(vectors)

    return sim

def get_recommendations(name, df, sim):
    idx = df[df["title"] == name].index[0]
    distance = list(enumerate(sim[idx]))

    distance = sorted(
        distance,reverse=True,key=lambda x: x[1]
    )

    movies = []

    for i in distance[1:11]:
        movies.append(df.iloc[i[0]].title)

    return movies
#print("Aryan RAj")
#Version 1
import streamlit as st

from src.preprocessing import get_data
from src.recommender import make_model
from src.recommender import get_recommendations

st.title("Netflix Recommendation System")
df = get_data()
sim = make_model(df)

selected_movie = st.selectbox(
    "Choose a movie",
    df["title"]
)

if st.button("Recommend"):
    result = get_recommendations(
        selected_movie,
        df,
        sim
    )

    st.write("Recommended Titles")

    for movie in result:
        st.write(movie)
import streamlit as st
import pickle
import random

# ---- Load pickled data ----
df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
df_old = pickle.load(open('movies_old.pkl', 'rb'))

# ---- Recommender functions (same as notebook) ----
def recommend(movie):
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [df.iloc[i[0]].title for i in movies_list]

mood_genres = {
    'Happy': ['Comedy', 'Animation', 'Family'],
    'Sad': ['Drama', 'Romance'],
    'Excited': ['Action', 'Adventure', 'Thriller'],
    'Stressed': ['Comedy', 'Animation']
}

def recommend_by_mood(mood):
    genres = mood_genres[mood]
    filtered = df_old[df_old['genres'].apply(lambda x: any(g in x for g in genres))]
    seed_movie = filtered.sample(1)['title'].values[0]
    recommendations = recommend(seed_movie)
    return seed_movie, recommendations

# ---- Streamlit UI ----
st.set_page_config(page_title="MoodFlicks", page_icon="🎬")
st.title("MoodFlicks 🎬")
st.write("Movie ya mood ke hisaab se recommendation lo!")

tab1, tab2 = st.tabs(["🎥 Movie se Recommend", "😊 Mood se Recommend"])

# ---- Tab 1: Movie-based recommendation ----
with tab1:
    st.subheader("Apni pasandeeda movie choose karo")
    selected_movie = st.selectbox(
        "Movie:",
        df['title'].values,
        key="movie_select"
    )
    if st.button("Recommend Karo", key="movie_btn"):
        recommendations = recommend(selected_movie)
        st.success(f"'{selected_movie}' jaisi movies:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"{i}. {movie}")

# ---- Tab 2: Mood-based recommendation ----
with tab2:
    st.subheader("Aaj tera mood kaisa hai?")
    selected_mood = st.selectbox(
        "Mood:",
        list(mood_genres.keys()),
        key="mood_select"
    )
    if st.button("Recommend Karo", key="mood_btn"):
        seed_movie, recommendations = recommend_by_mood(selected_mood)
        st.info(f"Tere mood ke hisaab se, ye try kar: **{seed_movie}**")
        st.success("Iske jaisi movies:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"{i}. {movie}")
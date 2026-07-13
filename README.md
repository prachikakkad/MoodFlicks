# MoodFlicks 🎬

A content-based movie recommendation system that suggests movies based on either a movie you like or your current mood.

## Features

- **Movie-based Recommendations**: Select a movie you enjoyed, and get 5 similar movies based on content similarity (genres, cast, keywords, etc.)
- **Mood-based Recommendations**: Choose your current mood (Happy, Sad, Excited, Stressed), and get movie suggestions matched to that vibe
- Built with a clean, interactive Streamlit UI

## How It Works

MoodFlicks uses **content-based filtering** to recommend movies:

1. Movie metadata (genres, cast, crew, keywords) is combined into a single "tags" field for each movie
2. `CountVectorizer` converts these tags into numerical vectors (bag-of-words, top 5000 features, English stop words removed)
3. **Cosine similarity** is computed between all movie vectors to measure how similar any two movies are
4. For a given movie, the top 5 most similar movies (by cosine similarity score) are returned

For mood-based recommendations, a movie is randomly sampled from genres associated with the selected mood (e.g., "Happy" → Comedy, Animation, Family), and that movie is then used as a seed for content-based recommendations.

## Tech Stack

- **Python**
- **Pandas** – data handling
- **Scikit-learn** – `CountVectorizer` and `cosine_similarity`
- **Streamlit** – web app UI
- **Pickle** – model/data serialization

## Project Structure

```
MoodFlicks/
├── app.py                 # Streamlit app
├── vectorizer.ipynb        # Notebook: vectorization, similarity computation, EDA
├── movies.pkl              # Processed movie data with tags
├── movies_old.pkl          # Original movie data (used for genre-based mood filtering)
├── similarity.pkl          # Precomputed cosine similarity matrix
├── requirements.txt
└── README.md
```

## Installation & Usage

1. Clone the repository
```bash
git clone https://github.com/prachikakkad/MoodFlicks.git
cd MoodFlicks
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run app.py
```

4. Open your browser at `http://localhost:8501`

## Future Improvements

- Add movie poster images via TMDB API
- Improve mood-genre mapping with more nuanced categories
- Add hybrid filtering (combine content-based with collaborative filtering)
- Deploy on Streamlit Cloud for live access

## Author

Prachi Kakkad

---

*Built as part of a Data Science / AI-ML learning journey, following [BunkBuddy](https://bunkbuddy-z76j.onrender.com/) as the first deployed project.*

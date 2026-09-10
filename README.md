# MoodFlicks 🎬 — Content & Mood-Based Movie Recommendation Engine

[![Live App](https://shields.io)](https://moodflicks.streamlit.app)

**MoodFlicks** is a web application utilizing content-based filtering and emotional mood mapping for movie recommendations. 

👉 **[Launch Live Demo](https://moodflicks.streamlit.app)**

### Core Features & Architecture
* **Content Similarity & Mood Mapping:** Computes cosine similarity via `CountVectorizer` and translates emotional inputs into genre distributions.
* **Tech Stack:** Python, Pandas, NumPy, Scikit-Learn, Streamlit.

### Installation & Local Setup
```bash
git clone https://github.com
cd MoodFlicks
pip install -r requirements.txt
streamlit run app.py
```
*(Access locally at `http://localhost:8501`)*

**Author:** Prachi Kakkad

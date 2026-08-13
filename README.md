# MoodFlicks 🎬 — Content & Mood-Based Movie Recommendation Engine

MoodFlicks is an interactive web application that implements content-based filtering pipelines to suggest films matching specific metadata features or active user emotional moods.

🚀 **Live Deployment:** [Launch MoodFlicks Live App](https://moodflicks.streamlit.app/) *(Update with your exact Streamlit link if different!)*

---

## ✨ Features

* **Content-Based Similarity Search:** Select a seed title to dynamically extract the top 5 closest matched films based on feature vector alignments.
* **Algorithmic Mood Mapping:** Matches real-time emotional inputs (Happy, Sad, Excited, Stressed) to specific target genre distributions before running content recommendation logic.
* **Streamlit UI Interface:** Completely responsive interface allowing fluid content selection and rapid prediction outputs.

---

## 🧠 How the Machine Learning Works

The recommendation pipeline converts qualitative text metadata into a dense spatial vector landscape:

1. **Feature Engineering:** Combines movie genres, cast lists, crew metrics, and keywords into a single consolidated string array ("tags") for every dataset asset.
2. **Text Vectorization:** Utilizes `CountVectorizer` to apply a Bag-of-Words text feature transformation (top 5000 feature tracking, automatic English stop-word filtering).
3. **Cosine Similarity Evaluation:** Generates a full spatial similarity matrix computing the mathematical cosine angle between all dense movie feature vectors.
4. **Seed Execution for Moods:** For mood parameters, the system randomly samples an optimized seed title from matching genre domains (e.g., *Happy* → Comedy, Animation, Family) to feed the core content matrix.

---

## 🛠️ Tech Stack & Dependencies

* **Core Language:** Python
* **Data Engineering:** Pandas
* **Machine Learning Modules:** Scikit-Learn (`CountVectorizer`, `cosine_similarity`)
* **Deployment & UI UI Layer:** Streamlit Architecture
* **Model Serialization:** Pickle Utility Engines

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/prachikakkad/MoodFlicks.git
cd MoodFlicks
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Local Development Instance
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501` to view your instance.

---

## 🎯 Future Optimization Pathways

* Integrate live movie poster assets by mapping production outputs to the external TMDB API layer.
* Transition core architecture into an advanced hybrid filtering framework (combining collaborative user weights with text-similarity profiles).

---

## 👤 Author
**Prachi Kakkad**  
*Built as a core milestone within a self-driven Data Science and AI-ML curriculum, following the initial BunkBuddy deployment pipeline.*

# 📚 Book Recommender System using Collaborative Filtering

This project is an intelligent **Book Recommendation System** built using **Collaborative Filtering (KNN)**. It recommends books based on user preferences by analyzing the similarity between users and books using a user-item interaction matrix.

## 🚀 Features

- 📊 User-Book rating matrix using pivot tables
- 🧠 KNN (K-Nearest Neighbors) model to find similar books
- ✅ Recommendation engine trained on real-world data
- 🗂️ Clean and modular code structure
- 🌐 Interactive Web UI using **Streamlit**
- 💾 Pickle-based model storage and loading
- 🛠 Configurable through YAML file

## 🧪 Tech Stack

- **Python 3.11+**
- **Pandas**, **NumPy**, **Scikit-Learn**
- **SciPy (CSR Matrix)**
- **Streamlit**
- **Pickle** for serialization
- **YAML** for config

## 🔧 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/books-recommender.git
cd books-recommender
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App

```bash
streamlit run app.py
```

## 🧠 How It Works

* The system uses a **user-item rating matrix** to understand the relationship between users and the books they rated.
* It then applies **KNN (using cosine distance)** to identify similar books.
* Based on a selected book, it suggests top similar books the user might enjoy.

## 📦 Model Artifacts

Trained models and data are stored in the `artifacts/` folder:

* `model.pkl`: Trained KNN model
* `book_pivot.pkl`: User-item pivot table
* `book_names.pkl`: List of unique book titles
* `final_rating.pkl`: Cleaned rating matrix

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Author

**Muhammad Hamza**
📧 [mr.hamxa942@gmail.com](mailto:mr.hamxa942@gmail.com)

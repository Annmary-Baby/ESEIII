import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# To set page
st.set_page_config(page_title="Data Visualizer", layout="centered", page_icon="📊")


st.title("📊 Text Similarity Analysis")

working_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dir}/data"

files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

selected_file = st.selectbox("Select a file", files_list, index=None)

if selected_file:

 
    file_path = os.path.join(folder_path, selected_file)

    df = pd.read_csv(file_path)

    # Replace NaN values 
    cols_to_fillna = ['Class Name', 'Department Name', 'Division Name']
    for col in cols_to_fillna:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Clean 
    df['Title'] = df['Title'].fillna('.')
    df['Review Text'] = df['Review Text'].fillna('.')

    # Text preprocessing function
    def preprocess_text(text):
        #lowercase
        text = text.lower()
        # Remove punctuation and special characters
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        # Tokenize text
        tokens = word_tokenize(text)
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]
        # Stemming
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return " ".join(lemmatized_tokens)

    df['Cleaned Text'] = df['Review Text'].apply(preprocess_text)

    # Display 
    st.subheader("Original Review Text:")
    st.write(df['Review Text'].head())

    st.subheader("Preprocessed Review Text:")
    st.write(df['Cleaned Text'].head())

    

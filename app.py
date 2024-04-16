import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st



# To set page 
st.set_page_config(page_title="Streamlit Web Application", layout="centered",page_icon="📊")

def show_about_page():
    st.title('About')
    st.write('Welcome to the About Page!')
    
    st.header('3D Plot Visualization')
    st.write('Use the different components of Streamlit to allow users to interactmwith the dataset, to explore and gain insights from the dataset.Create a 3-D plot to visualize the relationship between the Age,Rating,and Positive Feedbact Count columns.')
   
    
    st.header('Image Processing')
    st.write('This module generates a Streamlit component that allows the user to select the image processing techiques(Resize, Grayscale Conversion,Image cropping.Image Rotation) to apply on the given image and display the output')
  
    
    st.header('Text Similarity Analysis')
    st.write('The text analysis module performs text preprocessing on the the review text column,including tokenization,removing stopwords,punctuations,and special characters,and converting text to lowercase.Implement stemming,lemmatization to further normalize the text data.Using cosine similariy or jaccard similarity implement text similarity analysis to identify similar reviews within the dataset for General,General Petite, and intimates from the “ Division name” Column.') 
    
    
   

if __name__ == '__main__':
    show_about_page()




    


        
            








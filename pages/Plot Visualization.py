import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plots

# To set page
st.set_page_config(page_title="Data Visualizer", layout="centered", page_icon="📊")

st.title("📊 3D Plotting Visualization")

working_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = f"{working_dir}/data"

files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

selected_file = st.selectbox("Select a file", files_list, index=None)

if selected_file:

    file_path = os.path.join(folder_path, selected_file)

    df = pd.read_csv(file_path)

    cols_to_fillna = ['Class Name', 'Department Name', 'Division Name']
    for col in cols_to_fillna:
        df[col] = df[col].fillna(df[col].mode()[0])

    df['Title'] = df['Title'].fillna('.')
    df['Review Text'] = df['Review Text'].fillna('.')
    df = df.head(10)
    #display
    col1, col2 = st.columns(2)

    with col1:
        st.write("Sample Dataframe:")
        st.write(df.head())

    with col2:
        
        x_axis = st.selectbox("Select the X-axis", options=['Age', 'Rating', 'Positive Feedback Count'], index=None)
        y_axis = st.selectbox("Select the Y-axis", options=['Age', 'Rating', 'Positive Feedback Count'], index=None)
        z_axis = st.selectbox("Select the Z-axis", options=['Age', 'Rating', 'Positive Feedback Count'], index=None)
        plot_type = st.selectbox("Select 3D plot type", options=["Scatter Plot", "Bar Plot", "Line Plot"], index=0)

    # Button
    if st.button("Generate 3D Plot"):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')

        if plot_type == "Scatter Plot":
            ax.scatter(df[x_axis], df[y_axis], df[z_axis], c='r', marker='o')
        elif plot_type == "Bar Plot":
            ax.bar3d(df[x_axis], df[y_axis], 0, 1, 1, df[z_axis], shade=True)
        elif plot_type == "Line Plot":
            ax.plot(df[x_axis], df[y_axis], df[z_axis], marker='o')

        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_zlabel(z_axis)
        ax.set_title(f"3D {plot_type}: {x_axis} vs {y_axis} vs {z_axis}")

        # Show plot
        st.write(fig)

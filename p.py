import pickle
import streamlit as st
import pandas as pd 
import numpy as np
import requests

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movie_names = []
    for i in movie_list :
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names


st.header('Movie Recommender System')

movie_dict = pickle.load(open('movie_list.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values )

if st.button('Show Recommendation'):
    recomendation = recommend(selected_movie)
    for i in recomendation:
        st.write(i)
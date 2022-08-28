import pickle

import pandas as pd
import streamlit as st


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]     # get the index of the movie you want recommedations for
    # save the distances in sorted order of similarity
    distances=similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    # get only top 5 movies on the basis of similarity
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")


# load movie list to let user choose one
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

# create selectbox to select the movie for which you want recommendations
selected_movie=st.selectbox('Select the Movie for which you want to know similar movies',
                     movies['title'].values)

# select button to display
if st.button('Recommend'):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)



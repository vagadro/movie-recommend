**ML Project-RECOMMENDER SYSTEM- CONTENT BASED**

**Web app**: https://movie-recommmend.herokuapp.com/

**Overview:** Recommender systems are one of the most widely used machine learning based systems designed to recommend items to users on the basis of some similarilies. It is being used in almost every consumer facing industry like OTT platforms, ecommerce websites, food delivery apps, seach engines etc and has a huge potential in directing products KPI's in the right track. 
Recommender systems are generally build in product to drive DAU, MAU, YAU and target advertisements as per users past attributes and likeliness. 

Recommender systems generally works on two principles:
1) Content Based Recommendations: Product likeliness for user on the basis of content of the product/commodity
2) Collaborative Filtering based Recommendations: PRoduct likeliness for user on the basis of likeliness of the same product by "similar" other users 

In this project, I have tried to create a recommender system which recommends "similar" movies to user as per the selected movie on the basis of the content of the movies. 
The essence of any Recommender System is the "Similarity Matrix".
In case of Content Based recommendation system, this similarity matrix contains the similarity of a particular item to all the other items. This matrix is also sometimes reffered to as item-item similarity matrix. 

**Dataset used:** https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv
For building the model, we have used a dataset available in Kaggle by TMDB. The entire dataset is divided into two dataframes "Credits" and "Movies" having information like title, cast,crew, id, genres, language etc. 

**Approach:** 
- Data Loading: load both the files and merge
- EDA: identification of outliers, correlation between features and drop features which may not be very useful. 
- Data Cleaning and preprocessing: few of the columns like genres, keywords, crew and cast are in dictionaries, in order to extract features, convert them into list and extract features to create multiple tags for each movie. Tags will be the essential feature which will define the similarity between movies assuming that two similar movies will have similar tags (like same actor, same director, somewhat same overview etc)
- Model Building: Like mentioned earlier, in a recommender system the most important data is to create a similarity matrix. We created the item-item similarityu matrix using Cosine Similarity between movies and stored the dataset. 
- Deployment: Model deployed using Streamlit framewok using heroku server

In case you want to check out the same visit:  https://movie-recommmend.herokuapp.com/



Deepak Rawat

Linkedin: linkedin.com/in/deepak-rawat-183316b5

----------------------------------------------------------------------------------------------------------------------------------------------------------------



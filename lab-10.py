# Create a Streamlit app of your choice and deploy it using GitHub and Streamlit Community Cloud.  
# Your app should have at least two interactive elements and at least 
# one graph that updates based on the input. Submit the URL of your public Streamlit App. 

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('popular_names.csv')

st.title('Top 20 Most Popular Baby Names by Year')

user_input = st.slider('Select a Year:', 1910, 2021, 2021)
selected_option = st.selectbox('Select a Gender:', ['Male', 'Female'])
if selected_option == 'Male':
    sex = 'M'
else:
    sex = 'F'
data = df[(df['year'] == user_input) & (df['sex'] == sex)].sort_values('n', ascending = False).head(20)

fig = px.bar(data, x = 'name', y = 'n')

st.plotly_chart(fig)
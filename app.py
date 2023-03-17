import streamlit as st
from pathlib import Path
from PIL import Image

st.sidebar.image('Ratan_photo.jpg',width=200)

st.sidebar.title('About me')
st.sidebar.title('Education')
st.sidebar.title('Skills')
st.sidebar.title('Experiences')
st.sidebar.title('projects')
st.sidebar.title('acheivements')
st.sidebar.title('strengths')
st.sidebar.title('contacts')

#header

col1,col2 = st.columns(2) 
with col1:

    st.markdown("""
    #### Name : Ratan Kumar jha 
    ####  position : Data science
    
""")
  
    st.subheader('about')
    st.write('this is my about me')

#subheader
with col2:
    st.subheader('this is really great')

    #write
    st.write('this is a normal text')
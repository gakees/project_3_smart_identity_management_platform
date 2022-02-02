import streamlit as st
from PIL import Image


def app():
    image = Image.open('simplpic.png')
    st.image(image, caption=' ')
    st.title('Welcome')
    #page = st.selectbox("Menu", ["Home","Input", "Retrieve"]) 


# Custom imports 
#from multipage import MultiPage
#from pages import Home, Input, Retrieve # import your pages here

# Create an instance of the app 
#app = MultiPage()

# Title of the main page
# st.title("Input")

# Add all your applications (pages) here
# app.add_page("Input", Input.app)
# app.add_page("Retrieve", Retrieve.app)


# The main app

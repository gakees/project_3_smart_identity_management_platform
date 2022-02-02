# Imports

import streamlit as st
from PIL import Image


# Inpit.py
def app():
    image = Image.open('simplpic.png')
    st.image(image, caption=' ')
    st.title('Input')
    st.write('')
    st.markdown("## Store a Input Record in the Database")
# Add an input area where you can get a value for `sender` from the user.
# YOUR CODE HERE
    First_Name = st.text_input("Input First Name")
    Last_Name = st.text_input("Input Last Name")
    Birth_Date = st.text_input("Date of Birth MM/DD/YYYY")
    ID_Doc_Cat = st.selectbox("Enter ID Category",("Passport","Driver's Licence", "SSN"))
    ID_Doc_Num = st.text_input("Document Number")


# Input_database = {
#     "First Name": First_Name,
#     "Last Name": Last_Name,
#     "Birth Date": Birth_Date,
#     "ID Doc": ID_Doc_Cat,
#     "ID Doc Num":ID_Doc_Num,
# }

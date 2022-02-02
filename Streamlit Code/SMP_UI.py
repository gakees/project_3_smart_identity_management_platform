# Imports

import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib
from PIL import Image


# Create a Record Data Class that consists of the `sender`, `receiver`, and
# `amount` attributes

@dataclass
class Record: 
    sender: str
    receiver: str
    amount: float
    
#opening the image

image = Image.open('simplpic.png')



#displaying the image on streamlit app

st.image(image, caption=' ')
st.markdown("## Store a Input Record in the Database")

# Add an input area where you can get a value for `sender` from the user.
# YOUR CODE HERE
First_Name = st.text_input("Input First Name")

Last_Name = st.text_input("Input Last Name")

Birth_Date = st.text_input("Date of Birth MM/DD/YYYY")

ID_Doc_Cat = st.selectbox("Enter ID Category",("Passport","Driver's Licence", "SSN"))

ID_Doc_Num = st.text_input("Document Number")


Input_database = {
    "Fisrt Name": First_Name,
    "Last Name": Last_Name,
    "Birth Date": Birth_Date,
    "ID Doc": ID_Doc_Cat,
    "ID Doc Num":ID_Doc_Num,
}

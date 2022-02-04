import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib
from PIL import Image
import Home

def app():
    image = Image.open('simplpic.png')
    st.title('Retrieve Your Document')
    st.write('')
    ID_Doc_Cat = st.selectbox("Enter ID Category",("Passport","Driver's Licence", "SSN"))
    ID_Doc_Num = st.text_input("Document Number")
    
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib
from PIL import Image
import Home
import login
#from data.create_data import create_table




# image = Image.open('simplpic.png')
# st.image(image, caption=' ')

PAGES = {
    "Home": Home,
    "Login": login,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
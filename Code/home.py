import streamlit as st
from PIL import Image
from pinata import PinataClient
from contract import SmartContractClient

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    image = Image.open('../Images/simplpic.png')
    st.image(image)
    image = Image.open('../Images/home.png')
    st.image(image)
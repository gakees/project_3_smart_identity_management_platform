from PIL import Image
import streamlit as st
from pinata import PinataClient
from contract import SmartContractClient

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    image = Image.open('../Images/simplpic.png')
    st.image(image)
    st.write('')

    st.markdown("### Add Document")
    document_name = st.text_input("Enter Document Number")
    document_Category = st.selectbox("Enter Document Category", ("Driver's Licence", "Passport", "Social Security Number"))
    document_file_upload = st.file_uploader("Enter Document File (Upload)", type=["gif", "jpg", "jpeg", "pdf", "png", "tiff"])

    
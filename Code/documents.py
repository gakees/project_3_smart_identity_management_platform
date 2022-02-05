from PIL import Image
import streamlit as st
from pinata import PinataClient
from contract import SmartContractClient

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    image = Image.open('../Images/simplpic.png')
    st.image(image)
    st.write('')

    st.markdown("### Add Document")
    name = st.text_input("Enter Document Name")
    category = st.selectbox("Enter Document Category", ("Driver's Licence", "Passport", "Social Security Number"))
    file_to_upload = st.file_uploader("Enter Document File (Upload)", type=["gif", "jpg", "jpeg", "pdf", "png", "tiff"])

    if st.button("Add"):
        print(file_to_upload)
        print(contract.add_document(wallet, name, category, 'file.gif'))
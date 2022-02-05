import datetime
import streamlit as st
from PIL import Image
from pinata import PinataClient
from contract import SmartContractClient

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    image = Image.open('../Images/simplpic.png')
    st.image(image)
    st.write('')

    st.markdown("### Create Account")
    first_name = st.text_input("Enter First Name", "Glenn")
    middle_name = st.text_input("Enter Middle Name", "Aaron")
    last_name = st.text_input("Enter Last Name", "Kees")
    date_of_birth = st.date_input("Enter Date of Birth",
        value=datetime.date(1970, 1, 1),
        min_value=datetime.date(1960, 1, 1), 
        max_value=datetime.date(1999, 1, 1)).strftime("%m/%d/%Y")
    social_security_number = st.text_input("Enter Social Security Number", "123-45-6789")

    if st.button("Create"):
        print(contract.create_account(wallet, first_name, middle_name, last_name, date_of_birth, social_security_number))
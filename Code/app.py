import os
import home, login
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
from pinata import PinataClient
from contract import SmartContractClient

load_dotenv()
wallet = os.getenv("WALLET_ADDRESS")
pinata = PinataClient(os.getenv("PINATA_API_KEY"), os.getenv("PINATA_API_SECRET"))
contract = SmartContractClient(os.getenv("WEB3_PROVIDER_URI"), os.getenv("CONTRACT_ADDRESS"), Path("./Contracts/Compiled/SmartIdentityToken.abi.json"))

Navigation = {
    "Home": home,
    "Login": login,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(Navigation.keys()))
page = Navigation[selection]
page.app(pinata, contract, wallet)
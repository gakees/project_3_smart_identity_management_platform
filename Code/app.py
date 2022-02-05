import os
import home, login
import streamlit as st
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
from pinata import PinataClient
from contract import SmartContractClient

load_dotenv()
wallet = os.getenv("WALLET_ADDRESS")
web3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
pinata = PinataClient(os.getenv("PINATA_API_KEY"), os.getenv("PINATA_API_SECRET"))
contract = SmartContractClient(os.getenv("WEB3_PROVIDER_URI"), os.getenv("CONTRACT_ADDRESS"), Path("./Contracts/Compiled/SmartIdentityToken.abi.json"))

Navigation = {
    "Home": home,
    "Login": login,
}

for account in web3.eth.accounts:
    print(account)
    
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(Navigation.keys()))
page = Navigation[selection]
page.app(pinata, contract, wallet)
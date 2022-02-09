import os
import streamlit as st
import streamlit_authenticator as stauth
import home, account, documents
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

names = ["Brittany Jacques", "Debolina Mukherjee", "Glenn Kees", "Jaime Barragan", "Paul Rodriguez"]
usernames = ["bjacques", "dmukherjee", "gkees", "jbarragan", "prodriguez"]
passwords = ["test", "test", "test", "test", "test"]
cookie_expiration = 0

hashed_passwords = stauth.hasher(passwords).generate()
authenticator = stauth.authenticate(names, usernames, hashed_passwords, "SIMPL_COOKIE", "IMPL_SIGNATURE", cookie_expiration)
name, authentication_status = authenticator.login("login", "sidebar")
navigation = {"Home": home}
route = "Home"

if authentication_status:
    navigation = {
        "Account": account,
        "Documents": documents,
    }

    with st.sidebar:
        st.write("Welcome *%s*" % (name))

        st.write(" ")
        route = st.radio("Go to:", list(navigation.keys()))

        st.write(" ")
        wallet = st.selectbox("Select Wallet (address)", web3.eth.accounts)
elif authentication_status is None:
    pass
elif not authentication_status:
    st.sidebar.error('Username/password is incorrect')

page = navigation[route]
page.app(pinata, contract, wallet)
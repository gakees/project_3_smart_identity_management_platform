import streamlit as st
import streamlit_authenticator as stauth
import account, documents
from pinata import PinataClient
from contract import SmartContractClient

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    names = ['John Smith','Rebecca Briggs']
    usernames = ['jsmith','rbriggs']
    passwords = ['123','456']
    hashed_passwords = stauth.hasher(passwords).generate()

    authenticator = stauth.authenticate(
        names, 
        usernames, 
        hashed_passwords, 
        'some_cookie_name', 
        'some_signature_key')

    name, authentication_status = authenticator.login('Login', 'main')

    if authentication_status:
        st.write('Welcome *%s*' % (name))
        PAGES = {
            "Account": account,
            "Documents": documents,
        }

        st.title('Navigation')
        selection = st.radio("Go to", list(PAGES.keys()))
        page = PAGES[selection]
        page.app(pinata, contract, wallet)
    elif not authentication_status:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')        



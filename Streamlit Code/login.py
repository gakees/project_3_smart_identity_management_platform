import streamlit as st
import streamlit_authenticator as stauth
import Retrieve
import Input
def app():
    names = ['John Smith','Rebecca Briggs']
    usernames = ['jsmith','rbriggs']
    passwords = ['123','456']

    hashed_passwords = stauth.hasher(passwords).generate()

    authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=0)

    name, authentication_status = authenticator.login('Login','main')

    if authentication_status:
        st.write('Welcome *%s*' % (name))
        PAGES = {
            "Account": Input
            "Documents": Retrieve,
}

        st.title('Navigation')
        selection = st.radio("Go to", list(PAGES.keys()))
        page = PAGES[selection]
        page.app()
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')        



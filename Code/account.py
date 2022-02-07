import streamlit as st
import calendar
from PIL import Image
from pinata import PinataClient
from contract import SmartContractClient
from datetime import datetime, timedelta

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    image = Image.open('../Images/simplpic.png')
    st.image(image)
    st.write('')

    # Attempt to load the account (if it exists)
    account = Account(contract.get_account(wallet))

    if account.exists:
        st.markdown("### Update Account")
        st.write('')

        first_name = st.text_input("First Name", account.first_name)
        middle_name = st.text_input("Middle Name", account.middle_name)
        last_name = st.text_input("Last Name", account.last_name)
        date_of_birth = st.date_input("Date of Birth",
            value=account.date_of_birth,
            min_value=datetime(1900, 1, 1), 
            max_value=datetime(2000, 1, 1))
        social_security_number = st.text_input("Social Security Number", account.social_security_number)

        if st.button("Update Account"):
            update_account_receipt = contract.update_account(wallet, first_name, middle_name, last_name, calendar.timegm(date_of_birth.timetuple()), social_security_number)

    else:
        st.markdown("### Create Account")
        st.write('')

        first_name = st.text_input("First Name")
        middle_name = st.text_input("Middle Name")
        last_name = st.text_input("Last Name")
        date_of_birth = st.date_input("Date of Birth",
            min_value=datetime(1900, 1, 1), 
            max_value=datetime(2000, 1, 1))
        social_security_number = st.text_input("Social Security Number")

        if st.button("Create Account"):
            create_account_receipt = contract.create_account(wallet, first_name, middle_name, last_name, calendar.timegm(date_of_birth.timetuple()), social_security_number)

class Account:
    def __init__(self, account_tuple) -> None:
        if not (len(account_tuple)) == 6:
            self.exists = False
        else:
            self.exists = True
            self.owner = account_tuple[0]
            self.first_name = account_tuple[1]
            self.middle_name = account_tuple[2]
            self.last_name = account_tuple[3]
            self.date_of_birth = datetime(1970, 1, 1) + timedelta(seconds=account_tuple[4])
            self.social_security_number = account_tuple[5]
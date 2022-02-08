import streamlit as st
import calendar
from PIL import Image
from pinata import PinataClient
from contract import SmartContractClient
from datetime import datetime, timedelta
from web3.exceptions import ContractLogicError

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    image = Image.open('../Images/simplpic.png')
    st.image(image)
    st.write('')

    # Attempt to load the account (if it exists)
    try:
        account = Account(contract.get_account(wallet))
    except:
        account = Account(())

    if not account.exists:
        st.markdown("### Create Account")
        st.write('')
        st.markdown("***** denotes required field")
        with st.form(key="createDocument", clear_on_submit=True):
            first_name = st.text_input("First Name*").strip()
            middle_name = st.text_input("Middle Name").strip()
            last_name = st.text_input("Last Name*").strip()
            date_of_birth = st.date_input("Date of Birth*",
                value=datetime(1970, 1, 1),
                min_value=datetime(1900, 1, 1), 
                max_value=datetime(2000, 1, 1))
            social_security_number = st.text_input("Social Security Number*").strip()
            create_account_button = st.form_submit_button("Create Account")

        if create_account_button:
            try:
                create_account_receipt = contract.create_account(wallet, first_name, middle_name, last_name, calendar.timegm(date_of_birth.timetuple()), social_security_number)
                st.success("Account created successfully.")
            except (ContractLogicError, ValueError) as error:
                data = error.args[0]["data"]
                key = list(data.keys())[0]
                st.error(data[key]["reason"])
            except BaseException as error:
                st.error(f"An unknown error ocurred.\nMessage: {error}")

    else:
        st.markdown("### Update Account")
        st.write('')
        st.markdown("***** denotes required field")
        with st.form(key="updateDocument", clear_on_submit=False):
            first_name = st.text_input("First Name*", account.first_name).strip()
            middle_name = st.text_input("Middle Name", account.middle_name).strip()
            last_name = st.text_input("Last Name*", account.last_name).strip()
            date_of_birth = st.date_input("Date of Birth*",
                value=account.date_of_birth,
                min_value=datetime(1900, 1, 1), 
                max_value=datetime(2000, 1, 1))
            social_security_number = st.text_input("Social Security Number*", account.social_security_number).strip()
            update_account_button = st.form_submit_button("Update Account")

        if update_account_button:
            try:
                update_account_receipt = contract.update_account(wallet, first_name, middle_name, last_name, calendar.timegm(date_of_birth.timetuple()), social_security_number)
                st.success("Account updated successfully.")
            except (ContractLogicError, ValueError) as error:
                data = error.args[0]["data"]
                key = list(data.keys())[0]
                st.error(data[key]["reason"])
            except BaseException as error:
                st.error(f"An unknown error ocurred.\nMessage: {error}")

class Account:
    def __init__(self) -> None:
        self.exists = False
    def __init__(self, account_tuple) -> None:
        if not (len(account_tuple)) == 7:
            self.exists = False
        else:
            self.exists = True
            self.owner = account_tuple[0]
            self.first_name = account_tuple[1]
            self.middle_name = account_tuple[2]
            self.last_name = account_tuple[3]
            self.date_of_birth = datetime(1970, 1, 1) + timedelta(seconds=account_tuple[4])
            self.social_security_number = account_tuple[5]
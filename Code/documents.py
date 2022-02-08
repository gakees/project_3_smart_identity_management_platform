import pandas as pd
import streamlit as st
from PIL import Image
from pinata import PinataClient
from contract import SmartContractClient
from dataclasses import dataclass

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    image = Image.open('../Images/simplpic.png')
    st.image(image)
    st.write('')

    render_add_document_form(pinata, contract, wallet)
    st.write('')
    st.write('')
    render_existing_documents_form(pinata, contract, wallet)

def render_add_document_form(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    st.markdown("### Add Document")
    st.write('')
    
    with st.form(key="addDocument", clear_on_submit=True):
        name = st.text_input("Enter Document Name")
        category = st.selectbox("Enter Document Category", ("Driver's Licence", "Passport", "Social Security Number"))
        file_to_upload = st.file_uploader("Enter Document File (Upload)", type=["gif", "jpg", "jpeg", "pdf", "png", "tiff"], accept_multiple_files=False)
        add_document_button = st.form_submit_button("Add Document")

    if add_document_button:
        uri = pinata.upload_image(name, category, file_to_upload.getvalue())
        add_document_receipt = contract.add_document(wallet, name, category, uri)

def render_existing_documents_form(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    # Attempt to load the documents for the account (if any exist)
    documents = [Document(tuple) for tuple in contract.get_documents(wallet)]

    # Display existing documents (if applicable)
    if (len(documents)):
        documents_df = pd.DataFrame(documents)
        documents_df = documents_df.reset_index()
        documents_df = documents_df.iloc[:, 1:]
        documents_df = documents_df[documents_df["number"] > 0]
        documents_df.columns = ["Number", "Name", "Category", "Url"]

        # Only display the existing documents section when at least one exists
        if len(documents_df):
                st.markdown("### Existing Documents")
                st.write('')
                st.write(documents_df)
                st.write('')
        
                column1, column2, column3, column4 = st.columns([1, 1, 1, 1])
                with column1:
                    document_number = st.selectbox("Document Number", documents_df.Number)
                with column2:
                    st.write('')
                    st.write('')
                    remove_document_button = st.button("Remove Document")
                with column3:
                    st.empty()
                with column4:
                    st.empty()
                if remove_document_button:
                    remove_document_receipt = contract.remove_document(wallet, document_number)

@dataclass
class Document:
    number: int
    name: str
    category: str
    url: str

    def __init__(self, document_tuple):
        if not (len(document_tuple)) == 4:
            self.exists = False
        else:
            self.number = int(document_tuple[0])
            self.name = document_tuple[1]
            self.category = document_tuple[2]
            self.url = document_tuple[3]
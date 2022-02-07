from PIL import Image
import streamlit as st
from pinata import PinataClient
from contract import SmartContractClient

def app(pinata: PinataClient, contract: SmartContractClient, wallet: str):
    image = Image.open('../Images/simplpic.png')
    st.image(image)
    st.write('')

    st.markdown("### Add Document")
    st.write('')
    
    name = st.text_input("Enter Document Name")
    category = st.selectbox("Enter Document Category", ("Driver's Licence", "Passport", "Social Security Number"))
    file_to_upload = st.file_uploader("Enter Document File (Upload)", type=["gif", "jpg", "jpeg", "pdf", "png", "tiff"], accept_multiple_files=False)

    if st.button("Add Document"):
        uri = pinata.upload_image(name, category, file_to_upload.getvalue())
        add_document_receipt = contract.add_document(wallet, name, category, uri)

    # Attempt to load the documents for the account (if any exist)
    documents = [Document(tuple) for tuple in contract.get_documents(wallet)]

    if (len(documents)):
        pass

class Document:
    def __init__(self, document_tuple) -> None:
        if not (len(document_tuple)) == 4:
            self.exists = False
        else:
            self.exists = True
            self.number = document_tuple[0]
            self.name = document_tuple[1]
            self.category = document_tuple[2]
            self.uri = document_tuple[3]
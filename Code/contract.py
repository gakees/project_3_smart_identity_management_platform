import json
import calendar, time
from web3 import Web3

class SmartContractClient:
    def __init__(self, web3_provider_uri, contract_address, contract_abi_path, gas_amount=1000000):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider_uri))
        self.contract = self.__load_contract(contract_address, contract_abi_path)
        self.gas_amount = gas_amount

    def __load_contract(self, contract_address, contract_abi_path):

        # Load the contract ABI definition
        with open(contract_abi_path) as file:
            contract_abi = json.load(file)

        # Create an instance of the contract at address specified
        return self.web3.eth.contract(address=contract_address, abi=contract_abi)

    def to_epoch(self, date, format="%m/%d/%Y"):
        return calendar.timegm(time.strptime(date, format))

    def to_date(self, epoch, format="%m/%d/%Y"):
        return time.strftime(format, time.gmtime(epoch))

    def from_address(self, address):
        return {'from': address, 'gas': self.gas_amount}

    def create_account(self, address, first_name, middle_name, last_name, date_of_birth, social_security_number):
        # Call the createAccount() smart contract function
        hash = self.contract.functions.createAccount(
            first_name, 
            middle_name, 
            last_name, 
            self.to_epoch(date_of_birth), 
            social_security_number).transact(self.from_address(address))
        
        # Return the transaction receipt
        return self.web3.eth.waitForTransactionReceipt(hash)

    def get_account(self, address):
        # Call the getAccount() smart contract function
        hash = self.contract.functions.getAccount().transact(self.from_address(address))
        
        # Return the transaction receipt
        return self.web3.eth.waitForTransactionReceipt(hash)

    def update_account(self, address, first_name, middle_name, last_name, date_of_birth, social_security_number):
        # Call the updateAccount() smart contract function
        hash = self.contract.functions.updateAccount(
            first_name, 
            middle_name, 
            last_name, 
            self.to_epoch(date_of_birth), 
            social_security_number).transact(self.from_address(address))
        
        # Return the transaction receipt
        return self.web3.eth.waitForTransactionReceipt(hash)

    def add_document(self, address, name, category, uri):
        # Call the addDocument() smart contract function
        hash = self.contract.functions.addDocument(
            name, 
            category, 
            uri).transact(self.from_address(address))
        
        # Return the transaction receipt
        return self.web3.eth.waitForTransactionReceipt(hash)

    def get_documents(self, address):
        # Call the getDocuments() smart contract function
        hash = self.contract.functions.getDocuments().transact(self.from_address(address))
        
        # Return the transaction receipt
        return self.web3.eth.waitForTransactionReceipt(hash)

    def remove_document(self, address, number):
        # Call the removeDocument() smart contract function
        hash = self.contract.functions.getDocuments(number).transact(self.from_address(address))
        
        # Return the transaction receipt
        return self.web3.eth.waitForTransactionReceipt(hash)
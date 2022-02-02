pragma solidity ^0.5.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract SmartIdentityToken is ERC721Full ("SmartIdentityToken", "SMART") {

    mapping(address => Account) internal accounts;
    address payable contractOwner;

    constructor() public{
        contractOwner = msg.sender;
    }

    struct Account {
        address owner;
        string firstName;
        string middleName;
        string lastName;
        string emailAddres;
        uint dateOfBith;        
        string ssn;
        Document[] documents;
    }

    struct Document {
        uint number;
        string name;
        string category;
        string uri;
    }

    function createAccount(string memory firstName, string memory middleName, string memory lastName, string memory emailAddress, uint dateOfBirth, string memory ssn) public {
        // TODO: add the require guards for all of the inputs for this function

        address accountOwner = msg.sender;
        accounts[accountOwner] = Account(accountOwner, firstName, middleName, lastName, emailAddress, dateOfBirth, ssn);
    }

    //TODO: add an updateAccount() function...

    function addDocument(string memory documentName, string memory documentCategory, string memory documentURI) public returns (uint) {
        // TODO: addd guard logic here to prevent senders with no corresponding account to continue processing a token
        address accountOwner = msg.sender;
        Account storage account = accounts[accountOwner];

        uint documentNumber = totalSupply();
        _mint(accountOwner, documentNumber);
        _setTokenURI(documentNumber, documentURI);
        account.documents.push(Document(documentNumber, documentName, documentCategory, documentURI));

        return documentNumber;
    }

    //TODO: add a removeDocument() function...

    function getDocuments() public returns (memory Document[]) {
        // TODO: addd guard logic here to prevent senders with no corresponding account to continue processing a token
        address accountOwner = msg.sender;

        return accounts[accountOwner].documents;
    }    
}
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.11;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";

// Struct definitions for use in smart contracts for the
// Smart Identity Management Platform Layer (SIMPL)
library SmartIdentity {

    struct Account {
        address owner;
        string firstName;
        string middleName;
        string lastName;
        int32 dateOfBirth;        
        string ssn;
    }

    struct Document {
        uint number;
        string name;
        string category;
        string uri;
    }
}

// An NFT implementation of smart identity tokens to track identity documentation
contract SmartIdentityToken is ERC721 {
    address internal contractOwner;
    uint internal nextDocumentNumber;
    mapping(address => SmartIdentity.Account) internal accounts;
    mapping(address => SmartIdentity.Document[]) internal documents;

    constructor() ERC721("SmartIdentityToken", "SMART") {
        contractOwner = msg.sender;
        nextDocumentNumber++;
    }

    function createAccount(string memory firstName, string memory middleName, string memory lastName, int32 dateOfBirth, string memory ssn) public {
        require(accounts[msg.sender].owner == address(0), "Unauthorized usage.  Cannot execute createAccount()");
        // TODO: add the require guards for all of the inputs of this function

        accounts[msg.sender] = SmartIdentity.Account(msg.sender, firstName, middleName, lastName, dateOfBirth, ssn);
    }
    
    function getAccount() public view returns(SmartIdentity.Account memory) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot execute getAccount()");

        // Return the existing account (by owner)
        return accounts[msg.sender];        
    }

    function updateAccount(string memory firstName, string memory middleName, string memory lastName, int32 dateOfBirth, string memory ssn) public returns(SmartIdentity.Account memory) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot execute updateAccount()");
        // TODO: add the require guards for all of the inputs of this function

        // Update all of the fields (whether or not they were changed)
        accounts[msg.sender].firstName = firstName;
        accounts[msg.sender].middleName = middleName;
        accounts[msg.sender].lastName = lastName;
        accounts[msg.sender].dateOfBirth = dateOfBirth;
        accounts[msg.sender].ssn = ssn;

        // Return the updated account (by owner)
        return accounts[msg.sender];      
    }

    function addDocument(string memory name, string memory category, string memory uri) public returns (uint) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot execute addDocument()");
        // TODO: add the require guards for all of the inputs of this function

        uint number = nextDocumentNumber;
        _safeMint(msg.sender, number);
        documents[msg.sender].push(SmartIdentity.Document(number, name, category, uri));
        nextDocumentNumber++;

        // Return the number of the document added (by owner)
        return number;
    }

    function getDocuments() public view returns (SmartIdentity.Document[] memory) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot retrieve documents from account.");

        // Return the documents associated with account (by owner)
        return documents[msg.sender];
    }

    function removeDocument(uint number) public returns (SmartIdentity.Document[] memory) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot remove document from account.");
        require(number > 0, "The document number be greater than zero.");

        // Loop through the array of documents to find the correct one to remove
        for (uint index = 0; index < documents[msg.sender].length; index++) {
            if (documents[msg.sender][index].number == number) {
                delete documents[msg.sender][index];
                break;
            }
        }

        // Returns the documents with the specified document removed (by owner)
        return documents[msg.sender];
    }
}
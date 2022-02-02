// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";

// Struct definitions for use in smart contracts for the
// Smart Identity Management Platform Layer (SIMPL)
library SmartIdentity {

    struct Account {
        address owner;
        string firstName;
        string middleName;
        string lastName;
        string emailAddres;
        uint dateOfBith;        
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

    function createAccount(string memory firstName, string memory middleName, string memory lastName, string memory emailAddress, uint dateOfBirth, string memory ssn) public {
        require(accounts[msg.sender].owner == address(0), "Unauthorized usage.  Cannot execute createAccount()");
        // TODO: add the require guards for all of the inputs for this function

        accounts[msg.sender] = SmartIdentity.Account(msg.sender, firstName, middleName, lastName, emailAddress, dateOfBirth, ssn);
    }
    
    //TODO: add a getAccount() function...
    function getAccount() public view returns(SmartIdentity.Account memory) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot execute getAccount()");

        // Return account (by owner)
        return accounts[msg.sender];        
    }

    //TODO: add an updateAccount() function...

    function addDocument(string memory name, string memory category, string memory uri) public returns (uint) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot execute addDocument()");
        // TODO: add the require guards for all of the inputs for this function

        uint number = nextDocumentNumber;
        _safeMint(msg.sender, number);
        documents[msg.sender].push(SmartIdentity.Document(number, name, category, uri));
        nextDocumentNumber++;

        return number;
    }

    //TODO: add a removeDocument() function...

    function getDocuments() public view returns (SmartIdentity.Document[] memory) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot retrieve documents from account.");

        // Return documents associated with account (by owner)
        return documents[msg.sender];
    }    
}
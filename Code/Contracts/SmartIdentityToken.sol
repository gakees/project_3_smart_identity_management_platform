// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./SmartIdentity.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";

// An NFT implementation of smart identity tokens to track identity documentation
contract SmartIdentityToken is ERC721 {
    int64 constant MIN_AGE = 946746585;
    int64 constant MAX_AGE = -2208927015;
    address internal contractOwner;
    uint internal nextDocumentNumber;
    mapping(address => SmartIdentity.Account) internal accounts;
    mapping(address => SmartIdentity.Document[]) internal documents;

    event accountCreated(string, string, string);
    event accountUpdated(string, string, string);
    event documentAdded(string, string, string);
    event documentRemoved(address, uint);

    constructor() ERC721("SmartIdentityToken", "SMART") {
        contractOwner = msg.sender;
        nextDocumentNumber++;
    }

    function createAccount(string memory firstName, string memory middleName, string memory lastName, int64 dateOfBirth, string memory socialSecurityNumber) public {
        require(accounts[msg.sender].owner == address(0), "Unauthorized usage.  Cannot execute createAccount()");
        require(bytes(firstName).length > 0, "firstName is a required field");
        require(bytes(lastName).length > 0, "lastName is a required field");
        require(dateOfBirth <= MIN_AGE && dateOfBirth >= MAX_AGE, "dateOfBirth must be between 1/1/1900 and 1/1/2000");
        require(bytes(socialSecurityNumber).length > 0, "socialSecurityNumber is a required field");

        // Store the new account in the accounts mapping
        accounts[msg.sender] = SmartIdentity.Account(msg.sender, firstName, middleName, lastName, dateOfBirth, socialSecurityNumber);

        // Publish event to signal the account was created
        emit accountCreated(firstName, middleName, lastName);
    }
    
    function getAccount() public view returns(SmartIdentity.Account memory) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot execute getAccount()");

        // Return the existing account (by owner)
        return accounts[msg.sender];        
    }

    function updateAccount(string memory firstName, string memory middleName, string memory lastName, int64 dateOfBirth, string memory socialSecurityNumber) public returns(SmartIdentity.Account memory) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot execute updateAccount()");
        require(bytes(firstName).length > 0, "firstName is a required field");
        require(bytes(lastName).length > 0, "lastName is a required field");
        require(dateOfBirth <= MIN_AGE && dateOfBirth >= MAX_AGE, "dateOfBirth must be between 1/1/1900 and 1/1/2000");
        require(bytes(socialSecurityNumber).length > 0, "socialSecurityNumber is a required field");

        // Update all of the fields (whether or not they were changed)
        accounts[msg.sender].firstName = firstName;
        accounts[msg.sender].middleName = middleName;
        accounts[msg.sender].lastName = lastName;
        accounts[msg.sender].dateOfBirth = dateOfBirth;
        accounts[msg.sender].socialSecurityNumber = socialSecurityNumber;

        // Publish event to signal the account was updated
        emit accountUpdated(firstName, middleName, lastName);

        // Return the updated account (by owner)
        return accounts[msg.sender];      
    }

    function addDocument(string memory name, string memory category, string memory uri) public returns (uint) {
        require(accounts[msg.sender].owner != address(0), "Unauthorized usage.  Cannot execute addDocument()");
        require(bytes(name).length > 0, "name is a required field");
        require(bytes(category).length > 0, "category is a required field");
        require(bytes(uri).length > 0, "uri is a required field");

        uint number = nextDocumentNumber;
        _safeMint(msg.sender, number);
        documents[msg.sender].push(SmartIdentity.Document(number, name, category, uri));
        nextDocumentNumber++;

        // Publish event to signal the document was added
        emit documentAdded(name, category, uri);

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
                emit documentRemoved(msg.sender, number);
                break;
            }
        }

        // Returns the documents with the specified document removed (by owner)
        return documents[msg.sender];
    }
}
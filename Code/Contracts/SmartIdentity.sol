// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Struct definitions for use in smart contracts for the
// Smart Identity Management Platform Layer (SIMPL)
library SmartIdentity {

    struct Account {
        address owner;
        string firstName;
        string middleName;
        string lastName;
        int64 dateOfBirth;        
        string socialSecurityNumber;
        uint nextDocumentNumber;
    }

    struct Document {
        uint number;
        string name;
        string category;
        string uri;
    }
}
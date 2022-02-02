pragma solidity 0.5.1;

contract CustomerAccount{
    mapping(uint => Person) public people;
    uint256 public peopleCount = 0;

    address owner;

    modifier onlyOwner(){
        require(msg.sender == owner);
        _;
    }
    
    struct Person {
        uint _id;
        string _firstName;
        string _lastName;
        string _socialSecurity;
        }
    
    constructor() public{
        owner = msg.sender;
    }
    
    function addPerson(
        string memory _firstName, 
        string memory _lastName,
        string memory _socialSecurity
        ) 
        public onlyOwner {
        incrementCount;
        people[peopleCount] = Person(peopleCount, _firstName, _lastName, _socialSecurity);
    }

    function incrementCount() internal {
        peopleCount += 1;
    }
}

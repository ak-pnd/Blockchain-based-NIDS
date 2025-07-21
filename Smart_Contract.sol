#new_SM.sol(Solidity Smart Contract)

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract NIDSSignatures {
    event SignatureAdded(uint indexed id, string description, string hash, uint timestamp);

    struct Signature {
        uint id;
        string description;
        string hash;
        uint timestamp;
    }

    Signature[] public signatures;

    function addSignature(string memory description, string memory hash) public {
        uint id = signatures.length;
        signatures.push(Signature(id, description, hash, block.timestamp));
        emit SignatureAdded(id, description, hash, block.timestamp);
    }

    function getSignature(uint id) public view returns (string memory, string memory, uint) {
        Signature memory sig = signatures[id];
        return (sig.description, sig.hash, sig.timestamp);
    }

    function getSignaturesCount() public view returns (uint) {
        return signatures.length;
    }
}

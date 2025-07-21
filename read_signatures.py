# read_signatures.py
from web3 import Web3
import json
def view(contract_address):
	w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
	with open('new-build/NIDSSignatures.abi') as f:
	    abi = json.load(f)
	contract = w3.eth.contract(address=contract_address, abi=abi)

	count = contract.functions.getSignaturesCount().call()
	for i in range(count):
    		description, hash_value, timestamp = contract.functions.getSignature(i).call()
    		print(f"ID: {i}, Description: {description}, Hash: {hash_value}, Timestamp: {timestamp}")
	return

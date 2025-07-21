#deploy_smart_contract.py

import time
import json
import subprocess
from deploy_contract import creation,address
from read_signature import view
ALERT_FILE = '/var/log/snort/alert_json.txt'  # Update to your actual path

def parse_alert(alert_json):
    # Serialize all fields into a JSON string for storage
    all_fields = json.dumps(alert_json, sort_keys=True)
    # Use a hash of the serialized JSON as the unique hash
    hash_value = str(hash(all_fields))
    return all_fields, hash_value

def tail_alert_file(contract_address):
    with open(ALERT_FILE, 'r') as f:
        # Go to the end of the file
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            try:
                alert_json = json.loads(line)
                all_fields, hash_value = parse_alert(alert_json)
                creation(all_fields, hash_value,contract_address) 
                print(f"Submitted alert: {all_fields} - {hash_value}")
                
            except Exception as e:
                print(f"Error parsing or submitting alert: {e}")
if __name__ == "__main__":
    contract_address=str(address())
    try:
        tail_alert_file(contract_address)
        
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected.")
        user_input = input("Press 'V' to display block data before exit: ")
        if user_input.upper() == 'V':
            print("Displaying block data...")
            view(contract_address)
        else:
            print("Exiting without displaying block data.")

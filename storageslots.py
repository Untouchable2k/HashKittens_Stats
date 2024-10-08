from web3 import Web3

# Connect to Ethereum node (e.g., Infura or local node)
infura_url = "https://eth.llamarpc.com"  # Replace with your Infura URL
w3 = Web3(Web3.HTTPProvider(infura_url))

# Contract address
contract_address = "0xB6eD7644C69416d67B522e20bC294A9a9B405B31"  # Replace with your contract address

# Function to get storage value at a specific slot
def get_storage_at(contract_address, slot):
    # Convert slot index to hexadecimal and pad it to 32 bytes
    slot_hex = Web3.to_hex(Web3.to_bytes(slot).rjust(32, b'\x00'))
    
    # Get storage value at the given slot
    storage_value = w3.eth.get_storage_at(contract_address, slot_hex)
    return int.from_bytes(storage_value, byteorder='big')


# Fetch the first 20 storage slots
for slot in range(40):
    value = get_storage_at(contract_address, slot)
    print(f"Slot {slot}: {value}")


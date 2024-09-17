from ape import accounts, project

def main():
    # Use the default account loaded from the .env PRIVATE_KEY
    account = accounts.load("default")
    
    # Deploy the contract with an initial message
    initial_message = "Hello, Ape!"
    contract = account.deploy(project.MyContract, initial_message)

    print(f"Contract deployed at address: {contract.address}")

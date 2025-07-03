from encrypt.decrypt import init_decrypt
from encrypt.encrypt import init_encrypt

def console_encrypt():
    while True:
        action = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message (or 'exit' to quit): ")
        if action == 'encrypt':
            message = input("Enter the message to encrypt: ")
            encrypted_message = init_encrypt(message)
            print(f"Encrypted message: {encrypted_message}")
        elif action == 'decrypt':
            encrypted_message = input("Enter the message to decrypt: ")
            decrypted_message = init_decrypt(encrypted_message)
            print(f"Decrypted message: {decrypted_message}")
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

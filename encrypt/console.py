from decrypt import decrypt
from encrypt import encrypt

def console_encrypt():
    while True:
        action = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message (or 'exit' to quit): ")
        if action == 'encrypt':
            message = input("Enter the message to encrypt: ")
            key = input("Enter the encryption key: ")
            encrypted_message = encrypt(message, key)
            print(f"Encrypted message: {encrypted_message}")
        elif action == 'decrypt':
            encrypted_message = input("Enter the message to decrypt: ")
            key = input("Enter the decryption key: ")
            decrypted_message = decrypt(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

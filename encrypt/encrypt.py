import random

def init_encrypt(text):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"

    if len(text) == 0:
        print("Text is empty")
        return False

    letter_shift = random.randint(1, 5)
    number_shift = random.randint(1, 5)

    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + letter_shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
        elif char in number:
            index = number.index(char)
            new_index = (index + number_shift) % len(number)
            encrypted_text += number[new_index]
        else:
            encrypted_text += char

    return encrypted_text, letter_shift, number_shift

from encrypt import init_encrypt, alphabet, number

text = "Hello, World! 123"
encrypted_text, letter_shift, number_shift = init_encrypt(text)
def decrypt(encrypted_text, letter_shift, number_shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - letter_shift) % len(alphabet)
            decrypted_text += alphabet[new_index]
        elif char in number:
            index = number.index(char)
            new_index = (index - number_shift) % len(number)
            decrypted_text += number[new_index]
        else:
            decrypted_text += char

    return decrypted_text
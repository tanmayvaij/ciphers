def encrypt(plain_text, shift):

    cipher_text = ""

    for char in plain_text:
        cipher_text += chr((ord(char) + shift - 65) % 26 + 65)

    return cipher_text


def decrypt(cipher_text, shift):

    plain_text = ""

    for char in cipher_text:
        plain_text += chr((ord(char) - shift - 65) % 26 + 65)

    return plain_text


plain_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = 23

cipher_text = encrypt(plain_text, shift)
print(cipher_text)

decrypted_cipher_text = decrypt(cipher_text, shift)
print(decrypted_cipher_text)

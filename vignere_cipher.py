def encrypt(plain_text, key):

    cipher_text = ""

    for i in range(len(plain_text)):
        cipher_text += chr((ord(plain_text[i]) + ord(key[i % len(key)])) % 26 + 65)

    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""

    for i in range(len(cipher_text)):
        plain_text += chr((ord(cipher_text[i]) - ord(key[i % len(key)])) % 26 + 65)

    return plain_text


plain_text = "GEEKSFORGEEKS"
key = "AYUSH"

cipher = encrypt(plain_text, key)
print(cipher)

decrypted_cipher_text = decrypt(cipher, key)
print(decrypted_cipher_text)

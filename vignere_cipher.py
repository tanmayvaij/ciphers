def encrypt(text, key): 

    encrypted_text = ""

    for i in range(len(text)):
        encrypted_text += chr((ord(text[i]) + ord(key[i % len(key) ])) % 26 + 65)

    return encrypted_text

def decrypt(encrypted_text, key):

    decrypted_text = ""

    for i in range(len(encrypted_text)):
        decrypted_text += chr((ord(encrypted_text[i]) - ord(key[i % len(key) ])) % 26 + 65)

    return decrypted_text

text = "GEEKSFORGEEKS"
key = "AYUSH"

print(decrypt(encrypt(text, key), key))

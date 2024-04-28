def encrypt(text: str, shift: int) -> str:

    encrypted_text = ""

    for letter in text:
        encrypted_text += chr( (ord(letter) + shift - 65 ) % 26 + 65)

    return encrypted_text

def decrypt(encrypted_text: str, shift: int) -> str:

    decrypted_text = ""

    for letter in encrypted_text:
        decrypted_text += chr((ord(letter) - shift - 65) % 26 + 65)
    
    return decrypted_text

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = 23

encrypted_text = encrypt(text, shift)
print(encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print(decrypted_text)

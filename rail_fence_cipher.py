def encrypt(plain_text, key):

    cipher_text = ""

    matrix = [["" for _ in range(len(plain_text))] for _ in range(key)]

    j = 0
    for i in range(len(plain_text)):

        matrix[j][i] = plain_text[i]

        if j == 0:
            sign = 1
        if j == key - 1:
            sign = -1

        j += sign

    for row in range(key):
        for col in range(len(plain_text)):
            cipher_text += matrix[row][col]

    return cipher_text


def decrypt(cipher_text, key):

    plain_text = ""

    matrix = [["" for _ in range(len(cipher_text))] for _ in range(key)]

    j = 0
    for i in range(len(cipher_text)):

        matrix[j][i] = "*"

        if j == 0:
            sign = 1
        if j == key - 1:
            sign = -1

        j += sign

    k = 0
    for row in range(key):
        for col in range(len(cipher_text)):
            if matrix[row][col] == "*":
                matrix[row][col] = cipher_text[k]
                k += 1

    j = 0
    for i in range(len(cipher_text)):

        plain_text += matrix[j][i]

        if j == 0:
            sign = 1
        if j == key - 1:
            sign = -1

        j += sign

    return plain_text


plain_text = "GEEKSFORGEEKS"
key = 3

cipher_text = encrypt(plain_text, key)
print(cipher_text)

decrypted_cipher_text = decrypt(cipher_text, key)
print(decrypted_cipher_text)

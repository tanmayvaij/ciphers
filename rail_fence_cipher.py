def encrypt(text, key):

    encrypted_text = ""
    matrix = [ [ "" for _ in range(len(text)) ] for _ in range(key) ]
    j = 0

    for i in range(len(text)):
        matrix[j][i] = text[i]
        if j == key - 1: sign =- 1
        elif j == 0: sign = 1
        j += sign

    for i in range(key):
        for j in range(len(text)):
            if (matrix[i][j] != ""): encrypted_text += matrix[i][j]

    return encrypted_text


def decrypt(encrypted_text, key):
    
    decrypted_text = ""
    matrix = [ [ "" for _ in range(len(text)) ] for _ in range(key) ]
    j = 0

    for i in range(len(text)):
        matrix[j][i] = "*"
        if j == key - 1: sign =- 1
        elif j == 0: sign = 1
        j += sign

    k = 0
    for i in range(key):
        for j in range(len(text)):
            if (matrix[i][j] == "*"):  
                matrix[i][j] = encrypted_text[k]
                k+=1

    l = 0
    for i in range(len(text)):
        decrypted_text += matrix[l][i]
        if l == key - 1: sign =- 1
        elif l == 0: sign = 1
        l += sign

    return decrypted_text


text = "GEEKSFORGEEKS"
key = 3

print(decrypt(encrypt(text, key), key))

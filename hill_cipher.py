def key_to_matrix(key):

    matrix = [[0 for _ in range(3)] for _ in range(3)]

    k = 0
    for row in range(3):
        for col in range(3):
            matrix[row][col] = ord(key[k]) - 65
            k += 1

    return matrix


def text_to_matrix(text):

    matrix = [[0 for _ in range(1)] for _ in range(3)]

    k = 0
    for row in range(3):
        for col in range(1):
            matrix[row][col] = ord(text[k]) - 65
            k += 1

    return matrix


def matrix_multiplication(matrix1, matrix2):

    matrix = [[0 for _ in range(1)] for _ in range(3)]

    for i in range(3):
        for j in range(1):
            for k in range(3):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return matrix


def matrix_to_ciphertext(matrix):

    cipher_text = ""

    for i in range(3):
        for j in range(1):
            cipher_text += chr(matrix[i][j] % 26 + 65)

    return cipher_text


def encrypt(text, key):

    return matrix_to_ciphertext(
        matrix_multiplication(key_to_matrix(key), text_to_matrix(text))
    )


key = "GYBNQKURP"
text = "ACT"

print(encrypt(text, key))

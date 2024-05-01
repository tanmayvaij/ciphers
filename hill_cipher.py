def generate_key_char_code_matrix(key):
    matrix = [["" for _ in range(3)] for _ in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            matrix[i][j] = ord(key[k]) - 65
            k += 1
    return matrix


def generate_text_char_code_matrix(text):
    matrix = [["" for _ in range(1)] for _ in range(3)]
    k = 0
    for i in range(3):
        for j in range(1):
            matrix[i][j] = ord(text[k]) - 65
            k += 1
    return matrix


def matrix_multiplication(matrix1, matrix2):
    res_matrix = [[0 for _ in range(1)] for _ in range(3)]

    for i in range(3):
        for j in range(1):
            for k in range(3):
                res_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return res_matrix


def matrix_mod_26(matrix):

    for i in range(3):
        for j in range(1):
            matrix[i][j] = matrix[i][j] % 26

    return matrix


def generate_text_from_matrix(matrix):
    cipher_text = ""
    for i in range(3):
        for j in range(1):
            cipher_text += chr(matrix[i][j] + 65)

    return cipher_text


def encrypt(plaintext, key):
    matrix1 = generate_key_char_code_matrix(key)
    matrix2 = generate_text_char_code_matrix(plaintext)

    res_matrix = matrix_multiplication(matrix1, matrix2)
    matrix26 = matrix_mod_26(res_matrix)

    cipher_text = generate_text_from_matrix(matrix26)

    print(cipher_text)


plaintext = "ACT"
key = "GYBNQKURP"

encrypt(plaintext, key)

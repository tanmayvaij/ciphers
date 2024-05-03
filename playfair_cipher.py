from math import ceil


def generate_matrix(key):

    text = ""
    matrix = [["" for _ in range(5)] for _ in range(5)]

    for char in key + "abcdefgh.klmnopqrstuvwxyz":
        if char not in text:
            text += char

    k = 0
    for row in range(5):
        for col in range(5):
            matrix[row][col] = text[k]
            k += 1

    return matrix


def generate_digram_matrix(plain_text):

    rows = ceil(len(plain_text) / 2)

    digram = [["" for _ in range(2)] for _ in range(rows)]

    k = 0
    for row in range(rows):
        for col in range(2):
            digram[row][col] = plain_text[k]
            k += 1

    return digram


def find_pair_loc(matrix, pair):

    loc = [[], []]

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == pair[0]:
                loc[0] = [row, col]
            if matrix[row][col] == pair[1]:
                loc[1] = [row, col]

    return loc


def generate_cipher(matrix, digram):

    cipher_text = ""

    for pair in digram:

        loc = find_pair_loc(matrix, pair)

        if loc[0][0] == loc[1][0]:

            loc[0][1] = (loc[0][1] + 1) % 5
            loc[1][1] = (loc[1][1] + 1) % 5

            cipher_text += matrix[loc[0][0]][loc[0][1]] + matrix[loc[1][0]][loc[1][1]]

        elif loc[0][1] == loc[1][1]:

            loc[0][0] = (loc[0][0] + 1) % 5
            loc[1][0] = (loc[1][0] + 1) % 5

            cipher_text += matrix[loc[0][0]][loc[0][1]] + matrix[loc[1][0]][loc[1][1]]

        else:
            loc[0][1], loc[1][1] = loc[1][1], loc[0][1]
            cipher_text += matrix[loc[0][0]][loc[0][1]] + matrix[loc[1][0]][loc[1][1]]

    return cipher_text


def encrypt(plain_text, key):

    matrix = generate_matrix(key)
    digram_matrix = generate_digram_matrix(plain_text)
    cipher_text = generate_cipher(matrix, digram_matrix)

    return cipher_text


plain_text = "mosque"
key = "monarchy"

cipher_text = encrypt(plain_text, key)
print(cipher_text)

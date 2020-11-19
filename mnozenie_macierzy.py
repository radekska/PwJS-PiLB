"""
Napisz skrypt realizujący mnożenie dwóch macierzy o rozmiarach 8x8
"""

import random

def matrix_printer(matrix):
    matrix_len = len(matrix)
    for row in range(matrix_len):
        for col in range(matrix_len):
            print(matrix[row][col], end = ' ')
        print('')

def generate_matrix(size, min_value, max_value):
    matrix = [[random.randint(min_value, max_value) for col in range(size)] for row in range(size)]
    return matrix



def calculate_matrix_product(matrix_1, matrix_2):
    matrix_1_col_len = len(matrix_1[0])
    matrox_1_row_len = len(matrix_1)
    matrix_2_row_len = len(matrix_2)

    if matrix_1_col_len != matrix_2_row_len:
        raise ValueError('Macierze nie spełniają warunku mnozenia...')

    matrix_product = [[x for x in range(matrix_1_col_len)] for y in range(matrox_1_row_len)]


    for row in range(matrox_1_row_len):
        for col in range(matrix_1_col_len):
            temp = 0
            for pos in range(matrix_1_col_len):
                temp += matrix_1[row][pos] * matrix_2[pos][col]

            matrix_product[row][col] = temp

    return matrix_product




if __name__ == '__main__':
    matrix_1 = generate_matrix(8, -100, 100)
    matrix_2 = generate_matrix(8, -100, 100)

    print("### MATRIX 1 ###")
    matrix_printer(matrix_1)
    print("### MATRIX 2 ###")
    matrix_printer(matrix_2)

    product_matrix = calculate_matrix_product(matrix_1, matrix_2)
    
    print("### PRODUCT MATRIX  ###")
    matrix_printer(product_matrix)



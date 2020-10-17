import random

def matrix_printer(matrix):
    matrix_row_len = len(matrix)
    matrix_col_len = len(matrix[0])
    for row in range(matrix_row_len):
        for col in range(matrix_col_len):
            print(matrix[row][col], end = ' ')
        print('')

def generate_matrix(size, min_value, max_value):
    matrix = [[random.randint(min_value, max_value) for col in range(size)] for row in range(size)]
    return matrix

def extend_matrix(matrix):

    matrix_row_len = len(matrix)
    matrix_col_len = len(matrix[0])

    if matrix_row_len != matrix_col_len:
        raise ValueError('Macierz nie jest kwadratowa.')

    for i in range(2):
        matrix.append(matrix[i])
    return matrix


def calculate_determinant(matrix):
    matrix_row_len = len(matrix)
    if matrix_row_len == 1:
        return matrix[0][0]

    matrix_col_len = len(matrix[0])

    if matrix_row_len == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    if matrix_row_len == 3:
        matrix = extend_matrix(matrix)
        det = 0
        for row in range(matrix_row_len):
            for col in range(matrix_col_len):
                if row == 0:
                    det += matrix[col][row] * matrix[col+1][row+1] * matrix[col+2][row+2]
                elif row == 1:
                    det += (-matrix[col][row+1]) * (-matrix[col+1][row]) * (-matrix[col+2][row-1])
                elif row > 1:
                    return det
                    
    if matrix_row_len > 3:
        raise ValueError('Brak wsparcia dla większych macierzy.')


if __name__ == '__main__':
    matrix = generate_matrix(3, -100, 500)
    print("### MATRIX 1 ###")
    matrix_printer(matrix)

    print(calculate_determinant(matrix))


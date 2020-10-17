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



def calculate_matrix_sum(matrix_1, matrix_2):
    summary_matrix = list(list())
    matrix_1_len = len(matrix_1)
    matrix_2_len = len(matrix_2)

    if matrix_1_len != matrix_2_len:
        raise ValueError('Macierze mają rózne rozmiary...')

    summary_matrix = [[matrix_1[row][col] + matrix_2[row][col] for col in range(matrix_1_len)] for row in range(matrix_1_len)]

    return summary_matrix



if __name__ == '__main__':
    matrix_1 = generate_matrix(128, 12, 100)
    matrix_2 = generate_matrix(128, -10, 15)

    print("### MATRIX 1 ###")
    matrix_printer(matrix_1)
    print("### MATRIX 2 ###")
    matrix_printer(matrix_2)

    summary_matrix = calculate_matrix_sum(matrix_1, matrix_2)
    
    print("### SUMMARY MATRIX  ###")
    matrix_printer(summary_matrix)



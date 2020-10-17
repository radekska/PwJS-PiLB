def calculate_vector_product(vector_1, vector_2):
    vector_1_len = len(vector_1)
    vector_2_len = len(vector_2)

    if vector_1_len != vector_2_len:
        raise Exception('Dułgości wektorów są rózne...')
    
    vector_product = 0

    for vector_1_cor, vector_2_cor in zip(vector_1, vector_2):
        vector_product += vector_1_cor * vector_2_cor

    return vector_product


if __name__ == '__main__':
    v1 = [1, 2, 12, 4]
    v2 = [2, 4, 2, 8]

    print('Iloczyn skalarny: {wynik}'.format(wynik=calculate_vector_product(v1, v2)))
    
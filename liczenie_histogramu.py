import random
import threading
import matplotlib.pyplot as plot

from queue import Queue
from wyznacznik_macierzy import generate_matrix, calculate_determinant

def generate_data(number_of_threads, min_val=-10000, max_val=10000):
    data_to_calc = dict()

    for number in range(number_of_threads):
        matrix_1 = generate_matrix(3, min_val, max_val)

        thread = 'THREAD_{number}'.format(number=number)
        data_to_calc[thread] = matrix_1
       
    return data_to_calc

def get_thread_output(que_object, threads_list):
    """
    This function takes all threads as a list, iterate through it and then join (connect to main therad)
    every other thread. At the end of function it takes from queue returned data.
    """
    thread_outputs = list()
    for thread in threads_list:
        thread.join()

    while not que_object.empty():
        result = que_object.get()
        thread_outputs.append(result)
    return thread_outputs

def calculate_data(data_to_calc):
    """
    This function spawns multiple threads. Their count is speficied as len(data_to_calc),
    then adds them to queue in order to retrive output data when finished.
    """
    threads_list = list()
    threads_que = Queue()

    for _ , matrix in data_to_calc.items():
        calculate_thread = threading.Thread(target=lambda in_que, args: in_que.put(
            calculate_determinant(matrix)), args=(threads_que, matrix))

        calculate_thread.start()
        threads_list.append(calculate_thread)


    calculated_data = get_thread_output(threads_que, threads_list)
    return calculated_data


if __name__ == '__main__':
    data = generate_data(25000)
    calculated_data = calculate_data(data)

    # Generating histogram 
    plot.style.use('ggplot')
    plot.hist(calculated_data, bins=15)
    plot.show()
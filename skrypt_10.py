import random

def sort_number(numbers):

    numbers_len = len(numbers)
    
    for _ in range(numbers_len):
        for idx in range(numbers_len):
            if idx < numbers_len - 1:
                if numbers[idx] < numbers[idx+1]:
                    numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
    
    return numbers
    



def generate_random_numbers(numbers_count, start, end):
    return [random.randint(start, end) for _ in range(numbers_count)]

if __name__ == '__main__':
    random_numbers = generate_random_numbers(50, 10, 1000)
    sorted_numbers = sort_number(random_numbers)

    #Compare
    print(sorted_numbers == sorted(random_numbers, reverse=True)) 

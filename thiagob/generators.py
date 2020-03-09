import random

def generate_list_of_ints(length, max_number):
    result = []
    for i in range(length):
        result.append(random.randint(1, max_number))
    return result

if __name__ == '__main__':
    print(generate_list_of_ints(10, 9999999))
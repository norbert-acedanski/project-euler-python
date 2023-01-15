import math


def get_triangular_numbers_generator():
    triangular_number = 1
    boundary = 1
    while True:
        yield triangular_number
        boundary += 1
        triangular_number += boundary


def get_number_of_divisors_of_a_number(number: int) -> int:
    num_of_divisors = 2 if number > 1 else 1
    upper_bound = math.ceil(math.sqrt(number))
    if upper_bound ** 2 == number and number > 1:
        num_of_divisors += 1
    for divisor in range(2, upper_bound):
        if number % divisor == 0:
            num_of_divisors += 2
    return num_of_divisors


if __name__ == "__main__":
    number_of_divisors = 500
    for num in get_triangular_numbers_generator():
        if get_number_of_divisors_of_a_number(num) > number_of_divisors:
            print(num)
            break

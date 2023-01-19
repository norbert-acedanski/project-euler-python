import math
import itertools
from typing import List


def is_number_prime(number: int) -> bool:
    current_factor = 2
    while current_factor <= math.sqrt(number):
        if number % current_factor == 0:
            return False
        else:
            current_factor += 1
    return True


def pandigital_numbers_based_on_number_of_digits(number_of_digits: int) -> List[int]:
    if number_of_digits >= 10:
        raise ValueError("Number of digits must be at most 9!")
    return [int("".join(str(digit) for digit in number))
            for number in itertools.permutations(range(1, number_of_digits + 1), number_of_digits)]


if __name__ == "__main__":
    largest_pandigital_prime = -1
    for num_of_digits in range(1, 10):
        for pandigital_number in pandigital_numbers_based_on_number_of_digits(number_of_digits=num_of_digits):
            largest_pandigital_prime = pandigital_number if is_number_prime(number=pandigital_number) \
                else largest_pandigital_prime
    print(largest_pandigital_prime)

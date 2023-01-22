import itertools
import math
import string

from typing import List


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        data = file.readline()
    return data[1:-1].split('","')


def sum_word_indexes(word: str) -> int:
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in word)


def prime_number_generator():
    # Not simple, but faster
    prime_number = 2

    def _is_number_prime(number: int) -> bool:
        if number == 2 or number == 3 or number == 5 or number == 7:
            return True
        # If the last digit is even or ends with 5, then the number is not prime
        if any(digit == number % 10 for digit in (0, 2, 4, 5, 6, 8)):
            return False
        current_factor = 3
        while current_factor <= math.sqrt(number):
            # If the reminder is 5, we skip to the next factor (we checked it above)
            if current_factor % 10 == 5:
                current_factor += 2
                continue
            if number % current_factor == 0:
                return False
            else:
                current_factor += 2
        return True

    while True:
        if _is_number_prime(prime_number):
            yield prime_number
        prime_number += 1


def is_number_prime(number: int) -> bool:
    current_factor = 2
    while current_factor <= math.sqrt(number):
        if number % current_factor == 0:
            return False
        else:
            current_factor += 1
    return True if number != 1 else False


def factorial(number: int) -> int:
    result = 1
    for num in range(2, number + 1):
        result *= num
    return result


def pandigital_numbers_based_on_number_of_digits(number_of_digits: int, include_zero: bool = False):
    if include_zero:
        if number_of_digits > 10:
            raise ValueError("Number of digits must be at most 10!")
    else:
        if number_of_digits >= 10:
            raise ValueError("Number of digits must be at most 9!")
    for number in itertools.permutations(range(int(not include_zero),
                                               number_of_digits + int(not include_zero)), number_of_digits):
        yield int("".join(str(digit) for digit in number))

import functools
import itertools
import math
import string

from typing import List, Tuple


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        data = file.readline()
    return data[1:-1].split('","')


def read_file_with_multiple_lines(file_path: str) -> List[List[int]]:
    data = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            current_data = list(map(int, line.split()))
            data.append(current_data)
    return data


def sum_word_indexes(word: str) -> int:
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in word)


def prime_number_generator():
    # Not simple, but faster
    yield 2
    prime_number = 3

    def _is_number_prime(number: int) -> bool:
        if number == 3 or number == 5 or number == 7:
            return True
        # If the last digit ends with 5, then the number is not prime
        if number % 10 == 5:
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
        prime_number += 2


def is_number_prime(number: int) -> bool:
    current_factor = 2
    while current_factor <= math.sqrt(number):
        if number % current_factor == 0:
            return False
        else:
            current_factor += 1
    return True if number != 1 else False


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


def get_max_route_value_from_tree(triangle_array: List[List[int]]) -> int:
    lengths_of_routes = [triangle_array[0][0]]
    for row in triangle_array[1:]:
        new_lengths = [row[0] + lengths_of_routes[0]]
        for index, number in enumerate(row[1:-1]):
            new_lengths.append(number + max(lengths_of_routes[index: index + 2]))
        new_lengths.append(row[-1] + lengths_of_routes[-1])
        lengths_of_routes = new_lengths
    return max(lengths_of_routes)


def is_number_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


def calculate_large_exponent(base: int, exponent: int) -> str:
    digits = list(int(digit) for digit in reversed(str(base)))
    add = 0
    for _ in range(exponent - 1):
        for index in range(len(digits)):
            current_multiple = digits[index]*base
            # Replacement of add = (current_multiple + add)//10 and digits[index] = (current_multiple + add) % 10
            add, digits[index] = divmod(current_multiple + add, 10)
        if add != 0:
            digits.append(add)
            add = 0
    return "".join(reversed([str(digit) for digit in digits]))


def get_reduced_fractions(d: int) -> List[Tuple[int, int]]:
    reduced_fractions = set()
    for denominator in range(2, d + 1):
        for numerator in range(1, denominator):
            g = math.gcd(numerator, denominator)
            reduced_fractions.add((numerator//g, denominator//g))
    return sorted(reduced_fractions, key=lambda fraction: fraction[0]/fraction[1])


def pentagonal_number(num: int) -> int:
    return num*(3*num - 1)//2


@functools.cache
def number_of_partitions(number: int) -> int:
    """Based on an equation p(n) = Sum (-1)**(k - 1)*p(n - gk), where k != 0 and gk is a pentagonal number.
    https://en.wikipedia.org/wiki/Pentagonal_number_theorem"""
    if number == 0:
        return 1
    num_of_partitions = 0
    k_min = int((1 - math.sqrt(1 + 24*number))/6)
    k_max = int((1 + math.sqrt(1 + 24*number))/6)
    for k in range(k_min, k_max + 1):
        if k == 0:
            continue
        coefficient = int((-1)**(k - 1))
        num_of_partitions += coefficient*number_of_partitions(number - pentagonal_number(k))
    return num_of_partitions

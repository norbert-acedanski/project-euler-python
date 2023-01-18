import math


def prime_number_generator():
    prime_number = 2
    while True:
        if is_number_prime(prime_number):
            yield prime_number
        prime_number += 1


def is_number_prime(number: int) -> bool:
    current_factor = 2
    while current_factor <= math.sqrt(number):
        if number % current_factor == 0:
            return False
        else:
            current_factor += 1
    return True


def is_prime_circular(prime_number: int) -> bool:
    for number in generate_rotated_number(number=prime_number):
        if not is_number_prime(number):
            return False
    return True


def generate_rotated_number(number: int):
    for index in range(1, len(str(number))):
        yield int(str(number)[index:] + str(number)[:index])


if __name__ == "__main__":
    max_boundary = 1_000_000
    prime_count = 0
    for prime in prime_number_generator():
        if prime >= max_boundary:
            break
        if is_prime_circular(prime):
            prime_count += 1
    print(prime_count)

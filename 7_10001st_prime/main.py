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


if __name__ == "__main__":
    for prime_index, prime in enumerate(prime_number_generator(), 1):
        print(f"{prime_index}. {prime}")
        if prime_index == 10_001:
            break

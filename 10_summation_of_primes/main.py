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


def sum_primes(up_to: int) -> int:
    result = 0
    for prime in prime_number_generator():
        if prime >= up_to:
            break
        result += prime
    return result


if __name__ == "__main__":
    prime_limit = 2_000_000
    print(sum_primes(prime_limit))

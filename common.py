import math


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
    return True

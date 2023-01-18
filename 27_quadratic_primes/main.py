import math


def get_number_of_generated_consecutive_primes(a_value: int, b_value: int) -> int:
    n = 0
    while True:
        if is_number_prime(n*n + a_value*n + b_value):
            n += 1
        else:
            return n


def is_number_prime(number: int) -> bool:
    if number < 2:
        return False
    current_factor = 2
    while current_factor <= math.sqrt(number):
        if number % current_factor == 0:
            return False
        else:
            current_factor += 1
    return True


if __name__ == "__main__":
    product = 0
    max_number_of_primes = 0
    a_max_modulus_value, b_max_modulus_value = 1000, 1000
    for a in range(-a_max_modulus_value + 1, a_max_modulus_value):
        for b in range(-b_max_modulus_value + 1, b_max_modulus_value):
            if (new_max := get_number_of_generated_consecutive_primes(a, b)) > max_number_of_primes:
                max_number_of_primes = new_max
                product = a*b
    print(product)


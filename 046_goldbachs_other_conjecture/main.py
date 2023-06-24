import math

from common import is_number_prime, prime_number_generator


def is_number_sum_of_prime_and_twice_a_square(number: int) -> bool:
    for prime in prime_number_generator():
        if prime > number:
            return False
        difference = number - prime
        if difference % 2 != 0:
            continue
        squared_number = difference//2
        if squared_number != int(math.sqrt(squared_number))**2:
            continue
        return True


if __name__ == "__main__":
    odd_composite = 3
    while True:
        if not is_number_prime(odd_composite) and not is_number_sum_of_prime_and_twice_a_square(number=odd_composite):
            print(odd_composite)
            break
        odd_composite += 2

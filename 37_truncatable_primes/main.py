from common import is_number_prime


def potential_trancatable_prime_number_generator():
    prime_number = 11
    while True:
        if any(digit in str(prime_number) for digit in ("0", "4", "6", "8")) or \
                any(str(prime_number)[-1] == digit or str(prime_number)[0] == digit for digit in ("1", "9")) or \
                any(str(prime_number)[-1] in digit for digit in ("2", "5")):
            prime_number += 1
            continue
        if is_number_prime(prime_number):
            yield prime_number
        prime_number += 1


def is_prime_trancatable_both_ways(prime_number: int) -> bool:
    prime_number = str(prime_number)
    for index in range(1, len(prime_number)):
        if not is_number_prime(number=int(prime_number[index:])):
            return False
    for index in range(1, len(prime_number)):
        if not is_number_prime(number=int(prime_number[:-index])):
            return False
    return True


if __name__ == "__main__":
    number_of_primes_found = 0
    number_of_both_ways_trancatable_primes = 11
    sum_of_primes = 0
    for prime in potential_trancatable_prime_number_generator():
        if is_prime_trancatable_both_ways(prime_number=prime):
            sum_of_primes += prime
            number_of_primes_found += 1
        if number_of_primes_found == number_of_both_ways_trancatable_primes:
            break
    print(sum_of_primes)

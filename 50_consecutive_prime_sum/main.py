import time

from common import prime_number_generator


def get_largest_prime_sum_count(limit: int) -> int:
    number_of_primes_below_limit = len(primes_below_a_threshold)
    factor = 1
    while sum(primes_below_a_threshold[0:number_of_primes_below_limit//factor]) > limit:
        factor += 1
    for num_of_primes in range(number_of_primes_below_limit//factor, 1, -1):
        for start_index in range(0, number_of_primes_below_limit - num_of_primes + 1):
            potential_prime = sum(primes_below_a_threshold[start_index:start_index + num_of_primes])
            if potential_prime >= limit:
                break
            if potential_prime in primes_below_a_threshold:
                return potential_prime


if __name__ == "__main__":
    limit = 1_000_000
    primes_below_a_threshold = []
    for prime in prime_number_generator():
        if prime >= limit:
            break
        primes_below_a_threshold.append(prime)
    print(get_largest_prime_sum_count(limit=limit))

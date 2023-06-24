from common import prime_number_generator


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

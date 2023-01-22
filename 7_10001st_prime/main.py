from common import prime_number_generator


if __name__ == "__main__":
    index = 10_001
    for prime_index, prime in enumerate(prime_number_generator(), 1):
        if prime_index == index:
            print(prime)
            break

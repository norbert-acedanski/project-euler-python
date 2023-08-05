from common import prime_number_generator


if __name__ == "__main__":
    reminder_exceed_number = 10**10
    for prime_index, prime in enumerate(prime_number_generator(), 1):
        _, reminder = divmod((prime - 1)**prime_index + (prime + 1)**prime_index, prime**2)
        if reminder > reminder_exceed_number:
            print(prime_index)
            break

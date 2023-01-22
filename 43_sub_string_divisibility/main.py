from common import pandigital_numbers_based_on_number_of_digits


def are_sub_numbers_divisible_by_next_primes(number: int) -> bool:
    number_str = str(number)
    primes = (2, 3, 5, 7, 11, 13, 17)
    for prime_index, digit_index in enumerate(range(1, len(number_str) - 2)):
        if not int(number_str[digit_index:digit_index + 3]) % primes[prime_index] == 0:
            return False
    return True


if __name__ == "__main__":
    total_sum = 0
    for pandigital_number in pandigital_numbers_based_on_number_of_digits(number_of_digits=10, include_zero=True):
        if len(str(pandigital_number)) != 10:
            continue
        if are_sub_numbers_divisible_by_next_primes(number=pandigital_number):
            total_sum += pandigital_number
    print(total_sum)

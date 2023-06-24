from common import is_number_prime, pandigital_numbers_based_on_number_of_digits


if __name__ == "__main__":
    largest_pandigital_prime = -1
    for num_of_digits in range(1, 10):
        for pandigital_number in pandigital_numbers_based_on_number_of_digits(number_of_digits=num_of_digits):
            largest_pandigital_prime = pandigital_number if is_number_prime(number=pandigital_number) \
                else largest_pandigital_prime
    print(largest_pandigital_prime)

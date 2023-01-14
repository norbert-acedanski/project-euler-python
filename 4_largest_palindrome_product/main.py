from typing import Iterable

number_of_digits = 3
minimum_digit_number = int("1"*bool(number_of_digits - 1) + "0"*(number_of_digits - bool(number_of_digits - 1)))
maximum_digit_number = int("9"*number_of_digits)
minimum_number = minimum_digit_number**2
maximum_number = maximum_digit_number**2


def get_palindromes(min_boundary: int, max_boundary: int, reverse: bool = False) -> Iterable:
    if reverse:
        return (number for number in range(max_boundary, min_boundary - 1, -1) if is_number_palindrome(number))
    return (number for number in range(min_boundary, max_boundary + 1) if is_number_palindrome(number))


def get_larges_palindrome_that_is_a_product_of_n_digit_numbers(palindromes: Iterable, n: int) -> int:
    for number in palindromes:
        for factor in range(maximum_digit_number, int((maximum_digit_number + minimum_digit_number)/2), -1):
            if number % factor == 0 and len(str(number // factor)) == n:
                return number


def is_number_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]


if __name__ == "__main__":
    unfiltered_palindromes = get_palindromes(min_boundary=minimum_number, max_boundary=maximum_number, reverse=True)
    print(get_larges_palindrome_that_is_a_product_of_n_digit_numbers(unfiltered_palindromes, number_of_digits))

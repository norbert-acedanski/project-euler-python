from common import is_number_palindrome


def reverse_a_number(number: int) -> int:
    return int(str(number)[::-1])


if __name__ == "__main__":
    max_iterations, upper_limit, number_of_lychrel_numbers = 50, 10_000, 0
    for num in range(upper_limit):
        i = 0
        checked_number = num
        while i <= max_iterations:
            checked_number += reverse_a_number(checked_number)
            if is_number_palindrome(checked_number):
                break
            i += 1
        else:
            number_of_lychrel_numbers += 1
    print(number_of_lychrel_numbers)

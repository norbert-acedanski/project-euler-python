from typing import List


def calculate_decimal_multiplication_product_for_champernowse_s_constant(digit_indexes: List[int]) -> int:
    product, current_index, current_number = 1, 1, 1
    while current_index <= max(digit_indexes):
        for digit in str(current_number):
            if current_index in digit_indexes:
                product *= int(digit)
            current_index += 1
        current_number += 1
    return product


if __name__ == "__main__":
    list_of_decimal_indexes = [10**0, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6]
    print(calculate_decimal_multiplication_product_for_champernowse_s_constant(digit_indexes=list_of_decimal_indexes))

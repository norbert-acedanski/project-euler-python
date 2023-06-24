import itertools
import math

if __name__ == "__main__":
    for product_digits in itertools.product('0123456789', repeat=9):
        string_number = "".join(f"{fixed_digit}{product_digit}" for product_digit, fixed_digit in
                                itertools.zip_longest(product_digits, "1234567890", fillvalue=""))
        number = int(string_number)
        if math.isqrt(number)**2 == number:
            print(math.isqrt(number))  # TODO: Currently, it takes almost an hour to get the answer... find a better way
            break

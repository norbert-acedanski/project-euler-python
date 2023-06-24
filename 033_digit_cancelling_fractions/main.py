from typing import Iterable
from fractions import Fraction


def get_digit_cancelling_fractions():
    non_trivial_fractions = []
    for den in range(11, 100):
        for nom in range(11, den):
            if den % 10 == 0 or nom % 10 == 0:
                continue
            first_digit, second_digit = divmod(den, 10)
            if str(first_digit) not in str(nom):
                continue
            try:
                if int(str(nom).replace(str(first_digit), "", 1))/second_digit == nom/den:
                    non_trivial_fractions.append((nom, den))
                    continue
            except ZeroDivisionError:
                pass
            if str(second_digit) not in str(nom):
                continue
            try:
                if int(str(nom).replace(str(second_digit), "", 1))/first_digit == nom/den:
                    non_trivial_fractions.append((nom, den))
            except ZeroDivisionError:
                pass
    return non_trivial_fractions


def mul(__iterable: Iterable) -> int:
    result = 1
    for number in __iterable:
        result *= number
    return result


if __name__ == "__main__":
    digit_cancelling_fractions = get_digit_cancelling_fractions()
    nominator = mul(fraction[0] for fraction in digit_cancelling_fractions)
    denominator = mul(fraction[1] for fraction in digit_cancelling_fractions)
    print(Fraction(nominator, denominator).denominator)

import math
from decimal import getcontext, Decimal
NUMBER_LIMIT = 100
DIGIT_LIMIT = 100

getcontext().prec = DIGIT_LIMIT + len(str(math.sqrt(DIGIT_LIMIT))[:str(math.sqrt(DIGIT_LIMIT)).find(".")])


def digit_sum(num: str) -> int:
    return sum(int(digit) for digit in num)


if __name__ == "__main__":
    total = 0
    for number in range(1, NUMBER_LIMIT + 1):
        if math.sqrt(number) % 1 == 0:
            continue
        total += digit_sum(str(Decimal(number).sqrt()).replace(".", "")[:DIGIT_LIMIT])
    print(total)

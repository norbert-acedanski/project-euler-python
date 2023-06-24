from common import calculate_large_exponent

if __name__ == "__main__":
    base_number = 2
    power = 1000
    print(sum(int(digit) for digit in calculate_large_exponent(base=base_number, exponent=power)))

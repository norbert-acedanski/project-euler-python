from common import calculate_large_exponent

if __name__ == "__main__":
    limit = 100
    max_sum = 1
    for a in range(1, limit):
        for b in range(1, limit):
            if (potential_max := sum(int(digit) for digit in calculate_large_exponent(base=a, exponent=b))) > max_sum:
                max_sum = potential_max
    print(max_sum)

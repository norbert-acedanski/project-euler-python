import itertools

from common import number_of_partitions

if __name__ == "__main__":
    divisor = 1_000_000
    for number in itertools.count(2):
        if number_of_partitions(number) % divisor == 0:
            print(number)
            break

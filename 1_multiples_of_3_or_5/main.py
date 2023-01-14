def multiple_of_3_or_5(up_to: int):
    for number in range(1, up_to):
        if number % 3 == 0 or number % 5 == 0:
            yield number


if __name__ == '__main__':
    print(sum(multiple_of_3_or_5(1000)))


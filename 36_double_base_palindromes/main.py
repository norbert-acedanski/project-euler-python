


if __name__ == "__main__":
    target = 1_000_000
    numbers_sum = 0
    for num in range(1, target):
        if str(num) == str(num)[::-1] and bin(num)[2:] == bin(num)[2:][::-1]:
            numbers_sum += num
    print(numbers_sum)

def factorial(number: int) -> int:
    result = 1
    for num in range(2, number + 1):
        result *= num
    return result


if __name__ == "__main__":
    grid_size = 20
    print(int(factorial(2*grid_size)/(factorial(grid_size))**2))

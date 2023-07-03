def get_last_digits_of_numbers(a: int, base: int, p: int, b: int, digits: int) -> int:
    """Returns last n digits of a number with a form 'a*base^p + b'"""
    modulo_number = 1
    for _ in range(p):
        _, modulo_number = divmod(modulo_number*base, 10**digits)
    return (modulo_number*a + b) % 10**digits


if __name__ == "__main__":
    a = 28_433
    power = 7_830_457
    print(get_last_digits_of_numbers(a=a, base=2, p=power, b=1, digits=10))

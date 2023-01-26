import datetime


def number_of_days_falling_on_given_day_of_the_month(start: datetime.date, end: datetime.date, weekday: int, day: int) \
        -> int:
    """weekday starts at 1 and ends at 7 (Monday to Sunday)"""
    number_of_days = 0
    for month in range(start.month, 13):
        if datetime.date(start.year, month, day).isoweekday() == weekday:
            number_of_days += 1
    for year in range(start.year + 1, end.year):
        for month in range(1, 13):
            if datetime.date(year, month, day).isoweekday() == weekday:
                number_of_days += 1
    for month in range(1, end.month + 1):
        if datetime.date(end.year, month, day).isoweekday() == weekday:
            number_of_days += 1
    return number_of_days


if __name__ == "__main__":
    print(number_of_days_falling_on_given_day_of_the_month(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31), 7, 1))

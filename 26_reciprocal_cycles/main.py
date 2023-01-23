from typing import Dict


def calculate_decimal_expansion(number: int) -> Dict[str, str]:
    if number < 2:
        raise ValueError("Enter number greater than 1!")
    expansion = {"non-periodic expansion": None, "periodic expansion": ""}
    multiplied_reminder = 1
    decimal_expansion_list = []
    reminders_list = []
    while True:
        multiplied_reminder *= 10
        whole_division_product, reminder = divmod(multiplied_reminder, number)
        if reminder == 0:
            decimal_expansion_list.append(str(whole_division_product))
            period_index = -1
            break
        if (next_term := (multiplied_reminder, reminder)) in reminders_list:
            period_index = reminders_list.index(next_term)
            break
        decimal_expansion_list.append(str(whole_division_product))
        reminders_list.append(next_term)
        multiplied_reminder = reminder
    if period_index == -1:
        expansion["non-periodic expansion"] = "".join(decimal_expansion_list)
    else:
        expansion["non-periodic expansion"] = "".join(decimal_expansion_list[:period_index])
        expansion["periodic expansion"] = "".join(decimal_expansion_list[period_index:])
    return expansion


if __name__ == "__main__":
    longest_cycle_length = 0
    d_with_max_cycle = 1
    d_max_value = 1000
    for d in range(2, d_max_value):
        expansion = calculate_decimal_expansion(number=d)
        if (new_length := len(expansion["periodic expansion"])) > longest_cycle_length:
            longest_cycle_length = new_length
            d_with_max_cycle = d
    print(d_with_max_cycle)
    


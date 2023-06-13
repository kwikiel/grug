def truncate_number(number: float) -> float:
    integer_part = int(number) # round down to obtain integer part
    decimal_part = number - integer_part # subtract integer part from original number to get decimal part
    return decimal_part

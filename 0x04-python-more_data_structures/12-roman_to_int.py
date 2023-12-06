#!/usr/bin/python3
# Function that converst a roman numeral to an integer
def roman_to_int(roman_string):
    keys = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    roman_numerals = dict(zip(keys, values))
    if not roman_string or roman_string is None:
        return 0
    integer = 0
    for i in range(len(roman_string) - 1):
        if roman_numerals[roman_string[i]] < roman_numerals[roman_string[i+1]]:
            integer = integer - roman_numerals[roman_string[i]]
        else:
            integer = integer + roman_numerals[roman_string[i]]
    integer = integer + roman_numerals[roman_string[-1]]
    return integer


if __name__ == "__main__":
    roman_to_int(roman_string)

#!/usr/bin/python3
# Function that returns the weighted average of all integers tuple
def weight_average(my_list=[]):
    dividend, divisor, average = 0, 0, 0.0
    for i in my_list:
        dividend = dividend + i[0] * i[1]
        divisor = divisor + i[1]
    average = dividend / divisor
    return average


if __name__ == "__main__":
    weight_average(my_list)

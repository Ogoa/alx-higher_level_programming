#1/usr/bin/python3
# Function that divides element by element 2 lists
def list_division(my_list_1, my_list_2, list_length):
    result = []
    i = 0

    while i < list_length:
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        i = i + 1
    return result

            
if __name__ == "__main__":
    list_division(my_list_1, my_list_2, list_length)

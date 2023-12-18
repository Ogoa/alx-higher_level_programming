This directory contains files for the tasks done under the `0x05. Python - Exceptions` project.<br>


<br>`0-safe_print_list.py`<br>
A function that prints `x` elements of a list and prints the real number of elements printed.<br>
`x` represents the number of elements to print and can be bigger than the length of `my_list`.<br>
Prototype:
```
def safe_print_list(my_list=[], x=0):
```

<br>`1-safe_print_integer.py`<br>
A function that prints an integer with `"{:d}".format()`, followed by a new line.<br>Prototype:
```
def safe_print_integer(value):
```
`value` can be any type (integer, string, etc.)<br>
It returns `True` if `value` has been correctly printed (if it is an integer).

<br>`2-safe_print_list_integers.py`<br>
A function that prints the first `x` elements of a list and only integers, where `x` can be bigger than the number of elements in the list.<br>Prototype:
```
def safe_print_list_integers(my_list=[], x=0);
```
`my_list` can contain any type (integer, string, etc.)

<br>`3-safe_print_division.py`<br>
A function that divides 2 integers and prints the result, then returns the value of the division otherwise `None`.<br>
Prototype:
```
def safe_print_division(a, b):
```

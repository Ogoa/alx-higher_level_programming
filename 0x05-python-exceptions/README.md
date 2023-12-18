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

<br>`4-list_division.py`<br>
A function that divides element by element 2 lists then returns a new list with the quotients. `my_list_1` and `my_list_2` can contain any type(integer, string, etc.). `list_length` can be bigger than the length of both lists.<br>Prototype:
```
def list_division(my_list_1, my_list_2, list_length):
```

<br>`5-raise_exception.py`<br>
A function that raises a type exception.<br>
Prototype:
```
def raise_exception():
```

<br>`6-raise_exception_msg.py`<br>
A function that raises a name exception with a message.<br>
Prototype: `def raise_exception_msg(message=""):`

<br>`8-safe_function.py`<br>
A function that executes a function safely.

#!/usr/bin/pythton3
'''Definition of a class Node and a class SinglyLinkedList
Attributes:
    No module level attributes

'''


class Node:
    '''Defines a node of a singly linked list'''

    def __init__(self, data, next_node=None):
        '''Initialises the node

        Args:
            data (int): Data value of the node
            next_node (Node): Pointer to the next node

        '''

        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''Retrieves the data property of a node'''

        return self.__data

    @data.setter
    def data(self, value):
        '''Assigns a value to the data field of an instance

        Args:
            value (int): Value being assigned
        '''

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        '''Retrieves the next node being pointed to'''

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Assigns a Node address to the next_node field

        Args:
            value (Node): Address of a node Node
        '''

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    '''Defines a singly linked list'''

    def __init__(self):
        '''Initialises the linked list'''

        self.__head = None

    def sorted_insert(self, value):
        '''Inserts a new Node into the correct sorted position in the list

        Args:
            value (int): data value of the new node
        '''

        node = Node(value, None)  # Create a new node

        if self.__head is None or value < self.__head.data:
            node.next_node = self.__head
            self.__head = node
            return

        temp = self.__head
        while temp.next_node is not None and temp.next_node.data < value:
            temp = temp.next_node

        node.next_node = temp.next_node
        temp.next_node = node

    def __str__(self):
        '''Generates a string representation of the linked list'''

        full_list = []
        temp = self.__head

        while temp is not None:
            full_list.append(str(temp.data))
            temp = temp.next_node

        return "\n".join(full_list)

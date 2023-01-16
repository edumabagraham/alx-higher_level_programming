#!/usr/bin/python3

class Node:
    """
    Blueprint for a Node in a linked-list

    Attributes
    ----------
    data: int
    next_node: Node
    """

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """
    Attributes
    ----------
    head: Node
    head node of the linked-list
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """
        Prints the linked-list
        with the help of the __str__
        helper function
        """
        string = ""
        temp = self.__head

        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node

            if temp is not None:
                string += "\n"

        return string

    def sorted_insert(self, value):
        """
        Inserts a new value into a sorted
        linked-list
        """

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        temp = self.__head
        if value < temp.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        while (temp.next_node is not None) and (temp.next_node.data < value):
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
        return

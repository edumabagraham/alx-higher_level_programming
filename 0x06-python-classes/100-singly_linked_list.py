#!/usr/bin/python3

"""Singly linked list"""


class Node:
    """
    This class represents a node

    Attributes
    ----------
    data : int
    data in the node

    next_node : None or a Node
    points to the next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """
        Instantiates the data and
        next_node fields
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter
        """
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
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a Singly
    linked list
    """
    def __init__(self):
        """
        Attributes
        ----------
        head : Node
        head node of the linked list
        """
        self.__head = None

    def __str__(self):
        """
        String representation of singly
        linked list for printing
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
        Adds new node to a sorted linked
        list
        Attributes
        ----------
        data of the new node
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
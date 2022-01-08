"""Implement a Linked List data structure in Python."""

class Node:
    """Node for a Linked List with int data values."""
    def __init__(self, data: int = 0):
        self.data = data  # defaults to 0 if arg not passed
        self.next = None
    
class LinkedList:
    """Encapsulates a series of connected Nodes. Head value defaults to 0"""
    def __init__(self, arr: list[int] = None):
        # whyyy doesn't Python have method overloading
        if arr is not None and arr != []:
            a: Node = Node()
            temp: Node = a
            for val in arr:
                temp.next = Node(val)  # add new Node with val
                temp = temp.next  # shift to next Node
            self.head = a.next  # first node should be 0
        else:
            self.head = Node(0)
    
    def printList(self):
        """Print all nodes following the list"""
        a: Node = self.head  # copy reference to avoid mutating self.head
        # result: str = ""
        while a != None:
            print(a.data, end=" -> ")  # print inline with arrow after
            a = a.next
        print(a)  # "end" of list, should always be None
    
    def push(self, data: int):
        """Push a new Node to the front of the list."""
        temp = self.head  # store old head
        new_head = Node(data)  # make new Node with data, next = None
        new_head.next = temp  # new node = rest of old list
        self.head = new_head  # update self.head to change the pointer
    
    def append(self, data: int) -> None:
        """Append new Node to end of list."""
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            a: Node = self.head
            while a.next != None:
                a = a.next  # iterate to last node
            a.next = new_node  # add reference to new_node to end of list
    
    def insertAfter(self, key: int, data: int):
        """Insert new node after the first node that matches key."""
        if self.head == None:
            self.head = Node(data)
        else:
            a = self.head
            while a.next != None and a.data != key:
                a = a.next  # loop until we reach the end or we find the right Node
            if a.data == key:
                temp = a.next  # store rest of list
                a.next = Node(data)  # add new Node after a
                a.next.next = temp  # add rest of list after new node
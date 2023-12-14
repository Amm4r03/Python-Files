# implementation of a linked list in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

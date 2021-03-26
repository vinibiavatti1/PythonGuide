"""
Linked list

* A linked list is a linear collection of data elements whose order is not
  given by their physical placement in memory. Instead, each element points to
  the next
"""
from doctest import testmod


# Node class
class Node:
    """
    Used with the Linked List to create the node chain
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None


# Linked list class
class LinkedList:
    """
    A Linked List is a linear collection of data elements whose order is not
    given by their physical placement in memory. Instead, each element points
    to the next. These elements are called by node (See Node class).

    Create a linked list
    >>> linked_list = LinkedList()

    Append right
    >>> linked_list.append_right('Hi')
    >>> linked_list.append_right(3)
    >>> linked_list.append_right(True)
    >>> linked_list.root.value
    'Hi'
    >>> linked_list.root.next.value
    3
    >>> linked_list.root.next.next.value
    True
    >>> linked_list.root.next.next.next is None
    True

    Length
    >>> len(linked_list)
    3

    Get
    >>> linked_list.get(0)
    'Hi'
    >>> linked_list.get(len(linked_list) - 1)
    True
    >>> linked_list.get(999)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    Append Left
    >>> linked_list.append_left('Hello')
    >>> len(linked_list)
    4
    >>> linked_list.root.value
    'Hello'

    Iteration (iter)
    >>> iterator = iter(linked_list)
    >>> next(iterator)
    'Hello'
    >>> next(iterator)
    'Hi'
    >>> next(iterator)
    3
    >>> next(iterator)
    True
    >>> next(iterator)
    Traceback (most recent call last):
        ...
    StopIteration

    Remove
    >>> linked_list.remove(len(linked_list) - 1)
    >>> len(linked_list)
    3
    >>> linked_list.root.next.next.next is None
    True
    >>> linked_list.remove(0)
    >>> len(linked_list)
    0
    >>> linked_list.root is None
    True
    >>> linked_list.remove(999)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    Pop
    >>> linked_list.append_right('Hi')
    >>> linked_list.append_right(3)
    >>> linked_list.pop()
    3
    >>> linked_list.pop()
    'Hi'
    >>> len(linked_list)
    0
    >>> linked_list.pop()
    Traceback (most recent call last):
        ...
    IndexError: the linked list is empty
    """
    def __init__(self):
        """
        Construct Linked List
        """
        self.root = None

    def append(self, value):
        """
        Alias for append_right method
        """
        self.append_right(value)

    def append_right(self, value):
        """
        Add a new node to the right side of the list
        """
        if self.root is None:
            self.root = Node(value)
        else:
            node = self.root
            while node.next is not None:
                node = node.next
            node.next = Node(value)

    def append_left(self, value):
        """
        Add a new node to the left side of the list (as root)
        """
        node = Node(value)
        node.next = self.root
        self.root = node

    def remove(self, index):
        """
        Remove the node by index. If index is 0 (zero), the root node will be
        removed
        """
        if index >= self.__len__() or index < 0:
            raise IndexError('list index out of range')
        if index == 0:
            self.root = None
            return
        node = self.root
        i = 0
        while i < (index - 1):
            node = node.next
            i += 1
        node.next = None

    def get(self, index):
        """
        Get the value from the index
        """
        if index >= self.__len__() or index < 0:
            raise IndexError('list index out of range')
        if index == 0:
            return self.root.value
        node = self.root
        i = 0
        while i < index:
            node = node.next
            i += 1
        return node.value

    def pop(self):
        """
        Return and remove the last element of the list
        """
        if self.root is None:
            raise IndexError('the linked list is empty')
        node = self.root
        i = 0
        while node.next is not None:
            node = node.next
            i += 1
        self.remove(i)
        return node.value

    def __len__(self):
        """
        Get the length of the list
        """
        length = 0
        node = self.root
        while node is not None:
            length += 1
            node = node.next
        return length

    def __iter__(self):
        """
        Create an iterator based on the list
        """
        self.current_node = self.root
        return self

    def __next__(self):
        """
        Get the next node value from the list
        """
        current = self.current_node
        if current is None:
            raise StopIteration()
        self.current_node = self.current_node.next
        return current.value


# Tests
def tests():
    """
    Test the Linked list module
    """
    linked_list = LinkedList()

    # Append Right
    linked_list.append_right('Hi')
    linked_list.append_right(3)
    linked_list.append_right(True)
    assert linked_list.root.value == 'Hi'
    assert linked_list.root.next.value == 3
    assert linked_list.root.next.next.value is True
    assert linked_list.root.next.next.next is None

    # Length
    assert len(linked_list) == 3

    # Get
    assert linked_list.get(0) == 'Hi'
    assert linked_list.get(len(linked_list) - 1) is True
    try:
        linked_list.get(999)
        assert False, 'An Index error has to be thrown'
    except IndexError as err:
        assert isinstance(err, IndexError)

    # Append Left
    linked_list.append_left('Hello')
    assert len(linked_list) == 4
    assert linked_list.root.value == 'Hello'

    # Iteration (iter)
    iterator = iter(linked_list)
    assert next(iterator) == 'Hello'
    assert next(iterator) == 'Hi'
    assert next(iterator) == 3
    assert next(iterator) is True
    try:
        next(iterator)
        assert False, 'A StopIteration error has to be thrown'
    except StopIteration as err:
        assert isinstance(err, StopIteration)

    # Iteration (for)
    for i, val in enumerate(linked_list):
        if i == 0:
            assert val == 'Hello'
        elif i == len(linked_list) - 1:
            assert val is True

    # Remove
    linked_list.remove(len(linked_list) - 1)
    assert len(linked_list) == 3
    assert linked_list.root.next.next.next is None

    # Remove root
    linked_list.remove(0)
    assert len(linked_list) == 0
    assert linked_list.root is None
    try:
        linked_list.remove(999)
        assert False, 'An Index error has to be thrown'
    except IndexError as err:
        assert isinstance(err, IndexError)

    # Pop
    linked_list.append_right('Hi')
    linked_list.append_right(3)
    assert linked_list.pop() == 3
    assert linked_list.pop() == 'Hi'
    assert len(linked_list) == 0
    try:
        linked_list.pop()
        assert False, 'An Index error has to be thrown'
    except IndexError as err:
        assert isinstance(err, IndexError)


# Algorithm
if __name__ == '__main__':
    tests()
    testmod()

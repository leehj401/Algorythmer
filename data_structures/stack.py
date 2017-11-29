"""
    Stack
    -----
    A stack or LIFO (last in, first out) is an abstract data type that serves
    as a collection of elements, with two principal operations: push, which
    adds an element to the collection, and pop, which removes the last element
    that was added.

    Pseudo Code: https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29
"""

"""
    수직적인 자료구조이다 즉 위에값을 빼야 다른 값을 뺄 수 잇다.
    위에 써져있는것과 마찬가지로 Stack이고 큐와 비교가 많이 되는 개념이다.
"""


class Stack:

    def __init__(self):
        self.stack_list = []

    def add(self, value):
        """
        Add element at last

        Time Complexity:  O(1)
        """

        """
        값을 추가한다. LIFO
        """
        self.stack_list.append(value)

    def remove(self):
        """
        Remove element from last return value

        Time Complexity:  O(1)

        삭제 물론 맨위값이다.
        """

        return self.stack_list.pop()

    def is_empty(self):
        """
        1 value returned on empty 0 value returned on not empty

        Time Complexity:  O(1)
        """
        return not self.size()

    def size(self):
        """
        Return size of stack

        Time Complexity:  O(1)
        """
        return len(self.stack_list)

"""
    Queue
    -----
    A Queue is a linear data structure, or more abstractly a sequential
    collection. The entities in the collection are kept in order and the
    principal (or only) operations on the collection are the addition of
    entities to the rear terminal position, known as enqueue, and removal of
    entities from the front terminal position, known as dequeue. This makes the
    queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure,
    the first element added to the queue will be the first one to be removed.

    Pseudo Code: https://en.wikipedia.org/wiki/Queue_%28abstract_data_type%29
"""
"""
    Queue이고 수평적인 자료구조이다. LIFO에 전형적인 예시이다.
"""
from collections import deque


class Queue:

    def __init__(self):
        self._queue = deque([])

    def add(self, value):
        """
        Add element as the last item in the Queue.

        Worst Case Complexity:  O(1)
        """
        '''
        큐에 값을 넣는다
        '''
        self._queue.append(value)

    def remove(self):
        """
        Remove element from the front of the Queue and return it's value.

        Worst Case Complexity:  O(1)
        """
        '''
        값을 삭제해준다. 값은 무조건 줄슨것 처럼 먼저것이 먼저 나간다
        '''

        return self._queue.popleft()

    def is_empty(self):
        """
        Returns a boolean indicating if the Queue is empty.

        Worst Case Complexity:  O(1)
        """
        return not len(self._queue)

    def size(self):
        """
        Return size of the Queue.

        Worst Case Complexity:  O(1)
        """
        return len(self._queue)

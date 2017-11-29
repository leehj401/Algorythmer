"""
    Singly Linked List
    ------------------
    A linked list is a data structure consisting of a group of nodes which
    together represent a sequence. Under the simplest form, each node is
    composed of data and a reference (in other words, a link) to the next
    node in the sequence; more complex variants add additional links. This
    structure allows for efficient insertion or removal of elements from any
    position in the sequence.

    Pseudo Code: https://en.wikipedia.org/wiki/Linked_list
"""
"""
    싱글 링크드 리스트
    -----------------
    링크드 리스트는 구조가 많은데 그중에서도 가벼운데 쓰이고 이건 Head만 있고
    Tail은 없는 구조이다.
"""

class Node:
    '''
    하나하나 들어가잇는 노드이다
    
    init을 데이터와 다음값으로 해준다
    '''

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        """
        Add element to list

        Time Complexity:  O(N)

        노드를 추가해준다.
        """
        node = Node(value)
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def _search_node(self, value, remove=False):
        current = self.head
        previous = None

        while current:
            if current.data == value:
                break
            else:
                previous = current
                current = current.next

        if remove and current:
            if previous is None:  # Head node
                self.head = current.next
            else:  # None head node
                previous.set_next(current.next)
            self.size -= 1

        return current is not None

    def remove(self, value):
        """
        Remove element from list

        노드를 삭제해준다. 마지막Tail이 없기때문에 시간복잡도가 오래걸린다.

        Time Complexity:  O(N)
        """

        return self._search_node(value, True)

    def search(self, value):
        """
        Search for value in list

        Time Complexity:  O(N)

        찾고 싶은값을 패러미터로 넣어준다.
        """
        return self._search_node(value)

    def size(self):
        """
        Return size of list
        """
        return self.size

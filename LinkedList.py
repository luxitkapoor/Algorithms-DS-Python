class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.

        """
        if index > self.size - 1 or index < 0:
            return -1
        else:
            node = self.findnode(index)
            return node.value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new = Node(val)
        if index == self.size:
            self.addAtTail(val)
        elif index > self.size - 1:
            return None
        else:
            node = self.findnode(index)
            curr = node.prev
            new.next = curr.next
            curr.next.prev = new
            curr.next = new
            new.prev = curr
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.

        """

        if index > self.size - 1:
            return None
        else:
            node = self.findnode(index)
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1

    def findnode(self, index):
        i = 0
        curr = self.head.next
        while i < index:
            curr = curr.next
            i += 1
        return curr

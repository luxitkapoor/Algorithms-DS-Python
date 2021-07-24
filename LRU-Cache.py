class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = capacity
        self.store = {}

    def get(self, key: int) -> int:
        if key in self.store:
            n = self.store[key]
            self.removeFrom(n)
            self.addTo(n)
            return n.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.removeFrom(self.store[key])
            newNode = Node(key, value)
            self.addTo(newNode)
            self.store.pop(key)
            self.store[key] = newNode
        else:
            newNode = Node(key, value)
            self.addTo(newNode)
            self.store[key] = newNode
            if len(self.store) > self.size:
                node = self.tail.prev
                self.removeFrom(node)
                self.store.pop(node.key)

    def addTo(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def removeFrom(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

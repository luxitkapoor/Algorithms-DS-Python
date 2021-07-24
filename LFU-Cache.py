class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None
        self.c = 1


class CounterNode:
    def __init__(self, c):
        self.counter = c
        self.subList = LinkedList()
        self.data = {}
        self.next = None
        self.prev = None


class LinkedList():
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addTo(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def removeFrom(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToNode(self, node, pos):
        node.next = pos
        node.prev = pos.prev
        pos.prev = node


class LFUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.counter = {}
        self.counterList = LinkedList()
        # self.counter[1] = CounterNode(1)
        # self.counterList.addTo(self.counter[1])

    def checkEmpty(self, node):
        counterNode = node
        if counterNode.subList.head.next == counterNode.subList.tail:
            self.counterList.removeFrom(counterNode)
            self.counter.pop(counterNode.counter)

    def update(self, node):
        counterToMove = node.c
        nodeForCounter = self.counter[counterToMove]
        # nodeToMove = nodeForCounter.data[node.key]
        nodeForCounter.subList.removeFrom(nodeForCounter.data.pop(node.key))
        counterToMove += 1
        node.c += 1
        if counterToMove in self.counter:
            nodeForCounter = self.counter[counterToMove]
            newNode = Node(node.key, node.value)
            nodeForCounter.subList.addTo(newNode)
            nodeForCounter.data[node.key] = newNode
            self.checkEmpty(self.counter[counterToMove - 1])
        else:
            nodeForCounter = CounterNode(counterToMove)
            self.counterList.addToNode(nodeForCounter, self.counter[counterToMove - 1])

            # self.counterList.addTo(nodeForCounter)
            self.counter[counterToMove] = nodeForCounter
            newNode = Node(node.key, node.value)
            nodeForCounter.subList.addTo(newNode)
            nodeForCounter.data[node.key] = newNode
            self.checkEmpty(self.counter[counterToMove - 1])

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            value = node.value
            self.update(node)
            return value
        else:
            return -1

    def eviction(self):
        leastUsedCounter = self.counterList.tail.prev
        leastUsedElement = leastUsedCounter.subList.tail.prev
        self.cache.pop(leastUsedElement.key)
        leastUsedCounter.subList.removeFrom(leastUsedCounter.data.pop(leastUsedElement.key))
        self.checkEmpty(leastUsedCounter)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update(node)

        else:
            if len(self.cache) + 1 > self.size and self.size > 0:
                self.eviction()
            if 1 not in self.counter:
                self.counter[1] = CounterNode(1)
                self.counterList.addToNode(self.counter[1], self.counterList.tail)
            node = Node(key, value)
            self.cache[key] = node
            subCounter = self.counter[1]
            newNode = Node(key, value)
            subCounter.subList.addTo(newNode)
            subCounter.data[key] = newNode
            # if len(self.cache) > self.size:
            #     self.eviction()

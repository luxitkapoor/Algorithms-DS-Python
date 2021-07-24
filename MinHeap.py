class MinHeap:
    def __init__(self, size):
        self.heap = [i for i in range(1, size + 1)]

    def heapPop(self):
        # Popping root and replacting root with the last element in the array
        element, self.heap[0] = self.heap[0], self.heap[len(self.heap) - 1]
        self.heap.pop(len(self.heap) - 1)
        index = 0
        while (index * 2) + 1 <= len(self.heap) - 1:
            temp = (index * 2) + 1
            temp = self.findMin(temp)
            if self.heap[index] < self.heap[temp]:
                return element
            else:
                self.heap[index], self.heap[temp] = self.heap[temp], self.heap[index]
                index = temp

    def heapPush(self, element):
        self.heap.append(element)
        index = len(self.heap) - 1

        while (index - 1) // 2 >= 0:
            parent = (index - 1) // 2
            if self.heap[index] <= self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                return None

    def findMin(self, index):
        if index + 1 <= len(self.heap) - 1:
            if self.heap[index] < self.heap[index + 1]:
                return index
            else:
                return index + 1
        else:
            return index


a = MinHeap(10)
a.heapPop()
print(a.heap)
a.heapPush(3)
print(a.heap)

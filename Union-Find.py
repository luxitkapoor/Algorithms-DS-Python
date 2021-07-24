class QuickFind:
    '''Quick Find as the name suggest is an implementation of Union Find where the find operation works in constant time. However for union the worst case time complexity is O(N). Also if we were to do N Union operations, then the worst case time complextiy is O(n*n)
    '''

    def __init__(self, n):
        ''' Initialize an array with numbers from 0 to n-1. This takes O(n) time. Initially each element is part of its own component so its value points to itself'''
        self.arr = [i for i in range(0, n)]

    def find(self, p, q):
        ''' To find if two elements are connected we compare the value at their index. If the value is equal then the two are connected. This function runs in constant time as the name suggests.'''
        try:
            if self.arr[p] == self.arr[q]:
                return True
            else:
                return False
        except IndexError:
            print('Value out of range. Try Again!')

    def union(self, p, q):
        ''' The union function first checks if the two inputs are connected by calling find(). If the inputs are not connected then we perform the union operation. The function takes two values p and q. Here we loop over the array and change value to q at every index where the current value equals to p. Basically if a[i] is equal to p, then we change it to a[i] = q. Time complexity of union operation is O(N). 
        '''
        try:
            if self.find(p, q):
                print(f'{p} {q} are already connected')
                return None
            else:
                for i in range(0, len(self.arr)):
                    if self.arr[i] == p:
                        self.arr[i] = q

                print(f'{p} {q}')
        except IndexError:
            print('Value out of range. Try Again!')


class QuickUnion:
    def __init__(self, n, weighted=False):
        self.arr = [i for i in range(0, n)]
        if weighted:
            self.weighted = True
            self.size = [1] * n
        else:
            self.weighted = False

    def root(self, i):
        while self.arr[i] != i:
            i = self.arr[i]
        return i

    def find(self, p, q):
        try:
            p_root = self.root(p)
            q_root = self.root(q)
            if p_root == q_root:
                return True
            else:
                return False
        except IndexError:
            print('Values out of range. Try Again!')

    def union(self, p, q):
        try:
            p_root = self.root(p)
            q_root = self.root(q)
            if p_root != q_root:

                if self.weighted:
                    if self.size[p_root] >= self.size[q_root]:
                        self.arr[q_root] = p_root
                        self.size[p_root] += self.size[q_root]
                    else:
                        self.arr[p_root] = q_root
                        self.size[q_root] += self.size[p_root]
                else:
                    self.arr[p_root] = q_root
            else:
                print(f'{p} {q} are already connected')
        except IndexError:
            print('Value out of range. Try Again!')


a = QuickUnion(10, weighted=True)

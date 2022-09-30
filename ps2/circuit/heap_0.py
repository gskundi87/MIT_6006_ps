class MinHeap(object):
    def __init__(self):
        self.heap = [None]
        self.heapSize = 0

    def left(self, x):
        return 2*x

    def right(self, x):
        return 2*x + 1

    def parent(self, x):
        return x // 2

    def append(self, key):
        if key is None:
            raise ValueError('Cannot insert None in the heap')

        self.heap.append(key)
        self.heapSize += 1

        if self.heapSize == 1:
            return

        index = self.heapSize
        parent = self.parent(index)

        while True:
            if parent < 1 or key >= self.heap[parent]:
                return
            
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]

            index = parent
            parent = self.parent(index)

    def min(self):
        return self.heap[1]

    def pop(self):
        if self.heapSize == 0:
            return None

        if self.heapSize == 1:
            self.heapSize -= 1
            return self.heap.pop()

        self.heap[1], self.heap[self.heapSize] = self.heap[self.heapSize], self.heap[1]
        x = self.heap.pop()
        self.heapSize -= 1
        self.minHeapify(1)

        return x

    def minHeapify(self, index):
        l = self.left(index)
        r = self.right(index)
        
        if l <= self.heapSize and self.heap[l] < self.heap[index]:
            smallest = l
        else:
            smallest = index
            
        if r <= self.heapSize and self.heap[r] < self.heap[smallest]:
            smallest = r
            
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.minHeapify(smallest)

    def __len__(self):
        return self.heapSize

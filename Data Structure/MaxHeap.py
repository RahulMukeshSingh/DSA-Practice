class MaxHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def get_left_child(self, i):
        return (2 * i) + 1 #(2i) if index starts from 0 

    def get_right_child(self, i):
        return (2 * i) + 2 #(2i + 1) if index starts from 0            

    def get_parent(self, i):
        if i == 0: return 0
        return (i - 1) // 2

    def get_leaf_range(self):
        return [self.size // 2, self.size - 1]

    def max_heapify(self,i):
        left_child = self.get_left_child(i) 
        right_child = self.get_right_child(i)
        last_index = self.size - 1
        largest = i
        if left_child <= last_index and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child <= last_index and self.heap[right_child] > self.heap[largest]:
            largest = right_child 
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)     

    def build_max_heap(self, arr = None):
        if arr: 
            self.heap.extend(arr)
            self.size = len(arr)
        leaf_index = self.get_leaf_range()
        for i in range(leaf_index[0] - 1, -1, -1): #Non Leaf Nodes in descending order
            self.max_heapify(i)

    def get_max(self):
        if self.size < 1: raise IndexError('No element in heap')
        return self.heap[0]

    def get_min(self):
        if self.size < 1: raise IndexError('No element in heap')        
        leaf_index = self.get_leaf_range()
        min = leaf_index[0]
        for i in range(leaf_index[0], leaf_index + 1):
            if self.heap[i] < min: min = self.heap[i]
        return min

    def extract_max(self): #same as delete_max or pop_max
        size = self.size
        if size < 1: raise IndexError('No element in heap')
        max = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.max_heapify(0) #no need to call build_max_heap
        return max

    def exchange_parent(self, i):
        while i > 0 and self.heap[i] > self.heap[self.get_parent(i)]:
            parent = self.get_parent(i)
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def update_key(self, i, key):
        if key > self.heap[i]: #increase key
            self.heap[i] = key
            self.exhange_parent(i)
        elif key < self.heap[i]: #decrease_key
            self.heap[i] = key
            self.max_heapify(i)

    def insert(self, key):
        self.heap.append(key)
        self.size += 1
        self.exchange_parent(self.size - 1)

    def remove(self, i):
       key = self.heap.pop()
       self.size = 1
       self.heap[i] = key
       self.max_heapify(i)

    def remove_key(self,key):
        i = self.heap.index(key)
        self.remove(i)        

    def heap_sort(self):
        for i in range(self.size - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.max_heapify(0)
        return self.heap    

    
arr = [100,20,30,10,15,7,16]
max_heap = MaxHeap()
max_heap.build_max_heap(arr)
print(max_heap.heap_sort())


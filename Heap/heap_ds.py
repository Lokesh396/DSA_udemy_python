class Heap:

    def __init__(self):
        self.heap_array = [10, 20, 15, 12, 40, 25, 18]

    def heapify(self):
        n = len(self.heap_array)
        for i in range(n // 2 - 1, -1, -1):
            max_index = i
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2

            while left_child_index < n:
                if self.heap_array[left_child_index] > self.heap_array[max_index]:
                    max_index = left_child_index
                if right_child_index < n and self.heap_array[right_child_index] > self.heap_array[max_index]:
                    max_index = right_child_index

                if max_index == i:
                    break  # If no swap needed, stop the loop
                else:
                    self.heap_array[i], self.heap_array[max_index] = self.heap_array[max_index], self.heap_array[i]
                    i = max_index  # Update the current index to continue the loop
                    left_child_index = 2 * i + 1
                    right_child_index = 2 * i + 2
        print(self.heap_array)

    def insert(self, value: int):
        self.heap_array.append(value)
        self.heapify()

    def remove(self):
        self.heap_array.pop(0)
        self.heapify()

    def __repr__(self):
        return str(self.heap_array)


heap = Heap()
# heap.insert(10)
# heap.insert(20)
# heap.insert(15)
# heap.insert(12)
# heap.insert(40)
# heap.insert(25)
# heap.insert(18)
heap.heapify()

print(heap)

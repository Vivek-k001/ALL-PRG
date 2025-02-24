import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        return "Heap is empty!"

    def peek(self):
        if not self.is_empty():
            return self.heap[0]
        return "Heap is empty!"

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        print("Heap:", self.heap)

# Example usage
h = MinHeap()
h.push(15)
h.push(10)
h.push(30)
h.push(5)
h.display()  # Output: Heap: [5, 10, 30, 15]

print("Popped:", h.pop())  # Output: Popped: 5
print("Top Element:", h.peek())  # Output: Top Element: 10
h.display()

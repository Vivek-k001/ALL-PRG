class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self, key):
        temp = self.head

        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None

ll.delete(20)
ll.display()  # Output: 10 -> 30 -> None


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert element
    def enqueue(self, new_node):

        if self.front is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
            return

        self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front

    # Delete element
    def dequeue(self):

        if self.is_empty():
            print("Queue is Empty")
            return

        deleted = self.front.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        print("Deleted:", deleted)

    # Check whether queue is empty
    def is_empty(self):
        return self.front is None

    # Display front element
    def peek(self):

        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Front Element:", self.front.data)

    # Display queue
    def display(self):

        if self.is_empty():
            print("Queue is Empty")
            return

        temp = self.front

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.front:
                break

        print("(Back to Front)")


# Main program
q = CircularQueue()

q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))

print("Circular Queue:")
q.display()

print("\nPeek Operation:")
q.peek()

print("\nIs Empty:", q.is_empty())

print("\nDequeue Operation:")
q.dequeue()

print("\nAfter Dequeue:")
q.display()

print("\nEnqueue Operation:")
q.enqueue(Node(50))

q.display()

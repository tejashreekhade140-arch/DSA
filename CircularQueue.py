
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

        if self.front is None:
            print("Queue is Empty")
            return

        deleted = self.front.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        print("Deleted:", deleted)

    # Display elements
    def display(self):

        if self.front is None:
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

q.dequeue()

print("After Dequeue:")
q.display()

q.enqueue(Node(50))

print("After Enqueue:")
q.display()

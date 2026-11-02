
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # 1. Enqueue
    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # 2. Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Dequeued Element:", temp.value)

            self.front = self.front.next

            if self.front is None:
                self.rear = None

    # 3. Display
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front

            while temp:
                print(temp.value)
                temp = temp.next

    # 4. Reverse Queue using Stack
    def reverse(self):
        stack = []
        temp = self.front

        while temp:
            stack.append(temp.value)
            temp = temp.next

        self.front = self.rear = None

        while stack:
            self.enqueue(stack.pop())

    # 5. Merge Two Queues
    def merge(self, q2):
        q3 = Queue()

        temp = self.front

        while temp:
            q3.enqueue(temp.value)
            temp = temp.next

        temp = q2.front

        while temp:
            q3.enqueue(temp.value)
            temp = temp.next

        return q3

    # 6. Check Identical Queues
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.value != temp2.value:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1 is None and temp2 is None


# Main Program

q1 = Queue()
q2 = Queue()

# Enqueue elements into Queue 1
q1.enqueue(10)
q1.enqueue(22)
q1.enqueue(67)

print("Queue 1:")
q1.display()

# Enqueue elements into Queue 2
q2.enqueue(40)
q2.enqueue(50)
q2.enqueue(30)
q2.enqueue(40)

print("Queue 2:")
q2.display()

# Dequeue from Queue 1
q1.dequeue()

print("After Dequeue:")
q1.display()

# Reverse Queue 1
q1.reverse()

print("After reverse:")
q1.display()

# Merge both queues
q3 = q1.merge(q2)

print("After merging:")
q3.display()

# Check identical
print("Checking identical:")

if q1.identical(q2):
    print("Queues are identical")
else:
    print("Queues are not identical")

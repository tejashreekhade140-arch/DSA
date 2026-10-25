
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DCLL:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev

            new_node.next = self.head
            new_node.prev = last

            last.next = new_node
            self.head.prev = new_node

    # Display forward
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")

    # Display backward
    def reverse_display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head.prev

        while True:
            print(temp.data, end=" <-> ")
            temp = temp.prev

            if temp == self.head.prev:
                break

        print("(back to last)")


dcll = DCLL()

dcll.insert(10)
dcll.insert(20)
dcll.insert(30)

print("Forward:")
dcll.display()

print("Backward:")
dcll.reverse_display()

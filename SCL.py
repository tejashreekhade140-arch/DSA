
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Append node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # 2. Insert node at a given position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        # Insert at beginning
        if pos == 1:
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                new_node.next = self.head
                self.head = new_node
                temp.next = self.head
            return

        # Insert at other positions
        temp = self.head
        p = 1

        while p < pos - 1 and temp.next != self.head:
            temp = temp.next
            p += 1

        if temp is None or (temp.next == self.head and p < pos - 1):
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 3. Delete node at a given position
    def delete(self, pos):
        if self.head is None or pos < 1:
            print("Invalid position or empty list")
            return

        # Delete first node
        if pos == 1:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                self.head = self.head.next
                temp.next = self.head
            return

        # Delete node at another position
        temp = self.head
        p = 1

        while p < pos - 1 and temp.next != self.head:
            temp = temp.next
            p += 1

        if p != pos - 1 or temp.next == self.head:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # 4. Search for a value
    def search(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        pos = 1

        while True:
            if temp.data == value:
                print("Value found at position:", pos)
                return

            temp = temp.next
            pos += 1

            if temp == self.head:
                break

        print("Value not found")

    # 5. Print the list
    def print(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("List elements:", end=" ")

        while True:
            print(temp.data, end=" ")
            temp = temp.next

            if temp == self.head:
                break

        print()

    # 6. Reverse the circular linked list
    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return

        prev = None
        curr = self.head
        old_head = self.head

        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

            if curr == old_head:
                break

        old_head.next = prev
        self.head = prev


# Create Circular Linked List object
list = CircularLinkedList()

# Append nodes
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))

# Display list
list.print()

# Insert node at position 2
list.insert(Node(15), 2)
print("After insertion:")
list.print()

# Delete node at position 3
list.delete(3)
print("After deletion:")
list.print()

# Search for a value
list.search(30)

# Reverse the list
list.reverse()
print("After reversing:")
list.print()

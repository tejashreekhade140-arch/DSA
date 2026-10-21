class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List - Append
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and Print
    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert at Specific Position
    def insert_at_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete Nodes Having Negative Values
    def delete_negative(self):
        while self.head and self.head.data < 0:
            self.head = self.head.next

        temp = self.head

        while temp and temp.next:
            if temp.next.data < 0:
                temp.next = temp.next.next
            else:
                temp = temp.next

    def delete_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next

# Main Program
ll = LinkedList()

# Operation 1: Create
for value in [10, -20, 30, -40, 50]:
    ll.append(value)

print("Original Linked List:")
ll.traverse()

# Operation 2: Traverse
print("\nTraversing Linked List:")
ll.traverse()

# Operation 3: Insert at Position
ll.insert_at_position(25, 3)
print("\nAfter Inserting 25 at Position 3:")
ll.traverse()

# Operation 4: Delete Negative Values
ll.delete_negative()
print("\nAfter Deleting Negative Values:")
ll.traverse()

ll.delete_value(30)

print("After Deleting 30:")
ll.traverse()
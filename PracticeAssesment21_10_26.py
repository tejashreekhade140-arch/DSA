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


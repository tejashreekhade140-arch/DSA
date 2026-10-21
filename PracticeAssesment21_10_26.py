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




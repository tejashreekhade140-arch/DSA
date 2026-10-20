
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def traverse(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next
    # 3. Insert at Specific Position (1-based)
    def insert(self, data, position):
        new_node = Node(data)

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for _ in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node
    

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print("Node Values:")
ll.traverse()

ll.insert(25, 3)
print("After Inserting 25 at Position 3:")
ll.traverse()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List (Append node at end)
    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = newnode

    # 2. Traverse and print node values
    def print_list(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert node at a specific position
    def insert(self, data, pos):
        newnode = Node(data)

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            newnode.next = self.head
            self.head = newnode
            return

        temp = self.head
        p = 1

        while temp and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        newnode.next = temp.next
        temp.next = newnode

    # 4. Find middle node and print its value
    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # 5. Delete node by value
    def del_node(self, value):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = temp.next
            print("Node deleted:", value)
            return

        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("Node deleted:", value)
                return

            temp = temp.next

        print("Value is not present in the list")

    # 6. Reverse Linked List
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # 7. Sum of every two consecutive node values
    def sum_consecutive(self):
        temp = self.head

        if temp is None or temp.next is None:
            print("At least two nodes are required")
            return

        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


# Main program
list = LinkedList()

# 1. Create Linked List
list.append(10)
list.append(20)
list.append(30)
list.append(55)
list.append(48)

# 2. Traverse and print
print("Original Linked List:")
list.print_list()

# 3. Insert node at position 2
list.insert(100, 2)
print("\nAfter Inserting 100 at Position 2:")
list.print_list()

# 4. Find middle node
print("\nMiddle Node:")
list.find_middle()

# 5. Delete node
list.del_node(30)
print("\nAfter Deleting 30:")
list.print_list()

# 6. Reverse Linked List
list.reverse()
print("\nAfter Reversing:")
list.print_list()

# 7. Sum of consecutive nodes
print("\nSum of Every Two Consecutive Nodes:")
list.sum_consecutive()




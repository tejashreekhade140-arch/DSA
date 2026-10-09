class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Append node at the end
    def append(self, data):
        newnode = data

        if self.head is None:
            self.head = newnode
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = newnode

    # Insert node at given position
    def insert(self, new_node, pos):

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while p != pos - 1 and temp.next != None:
            temp = temp.next
            p += 1

        new_node.next = temp.next
        temp.next = new_node

    # Delete node by value
    def del_node(self, value):

        temp = self.head

        # Empty list
        if temp is None:
            print("List is empty")
            return

        # Delete first node
        if temp.data == value:
            self.head = temp.next
            return

        # Delete other nodes
        while temp.next:

            if temp.next.data == value:
                temp.next = temp.next.next
                return

            temp = temp.next

        print("Value is not there in the list")

    # Reverse linked list
    def reverse(self):

        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Print linked list
    def print(self):

        total = 0
        temp = self.head

        while temp:
            print(temp.data)
            total += temp.data
            temp = temp.next

        print("Total sum:", total)


# Create LinkedList object
list = LinkedList()

# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Append nodes
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(55))
list.append(Node(48))


print("Original List:")
list.print()


# Insert
list.insert(Node(100), 1)

print("\nAfter Inserting 100:")
list.print()


# Delete
list.del_node(30)

print("\nAfter Deleting 30:")
list.print()


# Reverse
list.reverse()

print("\nAfter Reversing:")
list.print()

#print sum of 2 consicutive nodes in SLL
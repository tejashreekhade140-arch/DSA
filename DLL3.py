
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def print(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        # Go to the last node
        while temp.next:
            temp = temp.next

        # Print in reverse order
        print("Reverse order:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev


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

list.print()

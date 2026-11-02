
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    # Push element into Stack
    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    # Pop element from Stack
    def pop(self):
        if self.isempty():
            print("Stack is Empty")
            return None
        else:
            temp = self.top
            self.top = self.top.next
            return temp.value

    # Reverse Stack using Another Stack
    def reverse(self):
        ss1 = Stack()

        temp = self.top

        while temp:
            ss1.push(Node(temp.value))
            temp = temp.next

        return ss1

    # Display Stack elements
    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top

            while temp:
                print(temp.value)
                temp = temp.next


# Reverse string using Stack
def reverse_string(string):

    ss = Stack()

    # Push every character into Stack
    for char in string:
        ss.push(Node(char))

    # Pop characters to create reversed string
    reversed_string = ""

    while not ss.isempty():
        reversed_string += ss.pop()

    return reversed_string


# Main program
ss = Stack()

ss.push(Node(20))
ss.push(Node(30))
ss.push(Node(40))
ss.push(Node(50))
ss.push(Node(60))
ss.push(Node(70))

print("Original Stack:")
ss.print()

print("\nPopped Element:", ss.pop())

# Reverse string
string = "TEJASHREE"

result = reverse_string(string)

print("\nOriginal String:", string)
print("Reversed String:", result)

# Reverse Stack using another Stack
ss1 = ss.reverse()

print("\nReversed Stack:")
ss1.print()

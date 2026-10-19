
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Append node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # Insert node at a given position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        # Insert at the beginning
        if pos == 1:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        # Find the previous node
        temp = self.head
        p = 1

        while temp is not None and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        # Connect the new node
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node
    def del_node(self, value):

        temp = self.head

        # Empty list
        if temp is None:
            print("List is empty")
            return

        # Delete first node
        if temp.data == value:
            self.head = self.head.next
            self.head.prev=None
        else:    
        # Delete other nodes
            while (temp.data!=value and temp):
                temp=temp.next
                if temp==None:
                    print("Value is not there in the list")                
                    return
            temp.prev.next=temp.next
            if temp.next:
                temp.next.prev=temp.prev
            temp=None
    # Write a function to count occurence of a no.in the DLL
    def count_occurence(self):
        temp=self.head
        while temp:
            if temp.data==num:
                count+=1
            temp=temp.next
        print("The occuernce :",Count)

    #Write function to swap 1 and last node in DLL
    def swap_firandlast(self):
        temp=node1=self.head # node1 is first node and 
        while temp.next: #temp is last node
            temp=temp.next

        temp.next=node1.next
        node1.next=None
        node1.prev=temp.prev
        temp.prev.next=node1
        temp.prev=None
        self.head=temp


        
    # Print nodes in forward order
    def print(self):
        temp = self.head

        print("List elements:", end=" ")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Create LinkedList object
list = LinkedList()

# Append nodes
list.append(Node(12))
list.append(Node(20))
list.append(Node(12))
list.append(Node(55))
list.append(Node(48))

# Display the list
list.print()

# Delete Data
list.del_node(48)



list.swap_firandlast()
list.print()

# Insert 15 at position 2
list.insert(Node(15), 2)

# Display after insertion
print("After insertion:")
list.print()

# Write a function to count occurence of a no.in the DLL

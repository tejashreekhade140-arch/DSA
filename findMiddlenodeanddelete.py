
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Append node at the end
    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = newnode

    # 2. Reverse a linked list
    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            nextnode = temp.next
            temp.next = prev
            prev = temp
            temp = nextnode

        self.head = prev

    # 3. Find and delete the middle node
    def findmid_del(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print("Middle Node:", self.head.data)
            self.head = None
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        print("Middle Node Deleted:", slow.data)
        prev.next = slow.next

    # 4. Delete first and last nodes
    def delfirst_last(self):
        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        self.head = self.head.next

        # If the list is now empty
        if self.head is None:
            return

        # Find the last node
        temp = self.head
        prev = None

        while temp.next:
            prev = temp
            temp = temp.next

        # Delete last node
        prev.next = None

    # 5. Delete alternate nodes
    # Keeps nodes at positions 1, 3, 5, ...
    def del_alternate(self):
        if self.head is None:
            print("List is empty")
            return

        prev = self.head
        temp = self.head.next

        while temp:
            prev.next = temp.next
            temp = prev.next

            if temp:
                prev = temp
                temp = prev.next

    # 6. Concatenate two linked lists
    def concatenate(self, list2):
        if list2.head is None:
            return

        if self.head is None:
            self.head = list2.head
            list2.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = list2.head

        # Transfer nodes to list1
        list2.head = None

    # 7. Print linked list
    def print(self):
        if self.head is None:
            print("List is empty")
            return

        print("List Elements:", end=" ")

        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Main program
list1 = LinkedList()

list1.append(30)
list1.append(40)
list1.append(50)
list1.append(55)

print("Original List:")
list1.print()

print("\nAfter Reversing:")
list1.reverse()
list1.print()

print("\nAfter Deleting First and Last Nodes:")
list1.delfirst_last()
list1.print()

print("\nAfter Deleting Alternate Nodes:")
list1.del_alternate()
list1.print()

print("\nMiddle Node Deletion Example:")
list3 = LinkedList()
list3.append(10)
list3.append(20)
list3.append(30)
list3.append(40)
list3.append(50)

list3.print()

list3.findmid_del()
list3.print()

print("\nConcatenation Example:")
list2 = LinkedList()
list2.append(60)
list2.append(70)
list2.append(80)

list1.concatenate(list2)
list1.print()

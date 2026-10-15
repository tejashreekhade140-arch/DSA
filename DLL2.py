#Write a function to print node value in reverse order in DLL
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

    def insert(self, new_node ,pos):
        temp=self.head
        if pos==1:
            new_node.next= self.head
            self.head.prev=new_node
            self.head=new_node
        else:
            p=1
            while(p!=pos-1):
                temp=temp.next
                p+=1
            temp.next=new_node
            new_node.prev=temp
            new_node.next=temp
            if temp.next:# Last position
                temp.next.prev=new_node

    def print(self):
        temp=self.head
        print("List elements:", end=" ")        
        while temp.next:
            temp=temp.next
        while(temp):
            print(temp.data, end=" ")
            temp=temp.prev

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


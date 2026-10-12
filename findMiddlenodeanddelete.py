#find middle node and delete this node 
class LinkedList:
    def reverse(self):#Reversing a Linked List
        prev=self.head
    def findmid_del(self):
        temp= temp1=self.head
        prev=None
        while temp1 and temp1.next:
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        print("Middle Node:", temp.data)

        prev.next=temp.next
        temp=None

#Write a function to delete first and last node in SLL
    def delfirst_last(self):
        #First Node
        temp1=self.head
        temp1=None
        prev=None
        temp=self.head=self.head.next
        while(temp.next):
            prev=temp
            temp=temp.next
        # delete last Node
        prev.next=None
        temp=None
  
#Delete Alternate Nodes in SLL
def del_alternate(self):
    prev=self.head
    temp=self.head.next
    while pre and temp:
        prev.next=temp.next
        temp=None #delete the node
        prev=prev.next
        if prev:
            temp=prev.next
#Calculate two SLLs
#Merge Sort
def concatenate(self):
    temp=self.head
    while(temp.next):
        temp=temp.next
    temp.newnode=list2.head

def print(self):
    print()
    print("List Elements:")
    temp=self.head
    while(temp):
        print(temp.data, end=" ")

list1=LinkedList()
n1=Node(10)
n2=Node(20)
list1.append(30)
list1.append(40)
list1.append(50)
list1.append(55)
list1.print()
list1.reverse()
list1.print()
list1.delfirst_last()
list1.print()
list1.del_alternate()
list1.print()
list2.append(33)
list2.append(44)
list2.append(55)
list2.append(56)
list2.concatenate()
class LinkedList:
    def del_node(self,value):
        prev=temp
        temp=temp.next
    if temp==None:
        print("Value is not there in the List")
    return
        prev.next=temp.next
        temp=None

#Reverse the nodes 
    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next.prev
            prev=curr
            curr=nextnode
        self.head.prev

# Print sum of 2 consecutive nodes in SLL
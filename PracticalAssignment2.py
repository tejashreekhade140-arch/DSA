class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None

    # Push element into a Stack
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            temp=self.top
            print("Poped Elements:", temp.value)
            self.top=self.top.next
            temp=None
    


    def reverse(self):
        temp=self.top
        print("Reverse Stack Using Another Stack:")
        while temp:
            
            ss1.push(Node(temp.value))
            temp=temp.next    

    def print(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            while temp:
                print(temp.value)
                temp=temp.next

ss=Stack()
ss1=Stack()
ss.push(Node(20))
ss.push(Node(30))
ss.push(Node(40))
ss.push(Node(50))
ss.push(Node(60))
ss.push(Node(70))

ss.print()

ss.pop()

ss.reverse()
ss1.print()




# Stack Implementation using LinkedList
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    
    def isempty(self):
        return self.top is None

    #Insert Element in a Stack
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node

    #remove element From Stack
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            print("Poped Elements:", temp.data)
            self.top=self.top.next
            temp=None

    #reverse the Stack using another Stack
    def reverse(self):
        temp=self.top
        while temp:
            st1.push(Node(temp.data))
            #prev=temp
            temp=temp.next
    #Compare Two Stacks
    def com_two_stacks(self):
            
    def print(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            print("Stack Contains...")
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next

st=Stack()
st1=Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.push(Node(60))

st.print()

st.pop()

st.print()

st.reverse()
st1.print()
# Binary Search Tree
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
        

class Binarysearchtree:
    def __init__(self):
        self.root=None
        self.cnt=0
        self.lcnt=0

    def insert(self,new_node):
        if self.root is None: #Creating the root Node
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: # Left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:                       # Right Subtree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    # Inorder Traversal (Left, Root, Right)  Inside the Class                    
    def inorder(self, temp): # Recursive Method
        if temp is None: #Terminating condition for recursive call
            return
        else:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            if temp.left is None and temp.right is None:
                self.lcnt+=1
            self.inorder(temp.right)
    def preorder(self,temp):
        if temp is None:
            return
        else:
            print(temp.data, end=" ")
            self.preorder(temp.left)  
            self.preorder(temp.right)
    def postorder(self,temp):
        if temp is None:
            return
        else:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data,end=" ")
    def find_minmax(self,temp):
        temmp=temp
        while temmp.left:
            temmp=temmp.left
        print("\nMim Value:",temmp.data)
        temmp=temp
        while temmp.right:
            temmp=temmp.right
        print("\nMim Value:",temmp.data)
"""
# Inorder Traversal (Left, Root, Right)  Outside the Class                    
def inorder(temp): # Recursive Method
    if temp is None: #Terminating condition for recursive call
        return
    else:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right) 
        """

bst=Binarysearchtree()
bst.insert(Node(10))
bst.insert(Node(5))
bst.insert(Node(2))
bst.insert(Node(25))
bst.insert(Node(13))
bst.insert(Node(40))

"""
#Outside the class Call
inorder(bst.root)
"""
print("\nInorder:")

#Inside the Class Call
bst.inorder(bst.root)
print("\nTotal No. of leaf nodes:",bst.lcnt)
print("\nNo. of Nodes:",bst.cnt)
print("\nPreorder:")
bst.preorder(bst.root)
print("\nPostorder:")
bst.postorder(bst.root)
bst.find_minmax(bst.root)
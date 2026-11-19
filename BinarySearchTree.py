# Binary Search Tree
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class Binarysearchtree:
    def __init__(self):
        self.root=None

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
def inorder(temp): # Recursive Method
    if temp is None: #Terminating condition for recursive call
        return
    else:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)

bst=Binarysearchtree()
bst.insert(Node(10))
bst.insert(Node(5))
bst.insert(Node(2))
bst.insert(Node(25))
bst.insert(Node(13))
bst.insert(Node(40))

inorder(bst.root)


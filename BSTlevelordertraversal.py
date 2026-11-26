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
                        self.cnt += 1
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
            if temp.left is not None and temp.right is not None:
                self.lcnt+=1
            self.inorder(temp.right)

    def level_order(self,temp):
        if temp is None:
            print("BST is empty")
            return
        arr=[]
        cnt=0 #For counting visited Node
        level=0
        arr.append(temp)
        while cnt<len(arr):
            node_count=len(arr)-cnt # No of nodes to be visited
            print("\nLevel:",level,"nodes:",end=" ")
            for i in range (node_count):
                temmp=arr[cnt]
                cnt+=1
                print(temmp.data,end=" ")
                if temmp.left:
                    arr.append(temmp.left)
                if temmp.right:
                    arr.append(temmp.right)
            level+=1
    
bst=Binarysearchtree()
bst.insert(Node(10))
bst.insert(Node(5))
bst.insert(Node(2))
bst.insert(Node(25))
bst.insert(Node(13))
bst.insert(Node(40))

print("\nInorder:")
bst.inorder(bst.root)

print("\nLevel order:")

bst.level_order(bst.root)



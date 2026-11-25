
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        break
                    temp = temp.right

    # Inorder
    def inorder(self, temp):
        if temp:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)

    # Search
    def search(self, key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    # Minimum
    def minimum(self, temp):
        while temp.left:
            temp = temp.left
        return temp.data

    # Maximum
    def maximum(self, temp):
        while temp.right:
            temp = temp.right
        return temp.data

    # Delete
    def delete(self, temp, key):
        if temp is None:
            return None

        if key < temp.data:
            temp.left = self.delete(temp.left, key)

        elif key > temp.data:
            temp.right = self.delete(temp.right, key)

        else:
            if temp.left is None:
                return temp.right
            elif temp.right is None:
                return temp.left

            # Inorder Successor
            succ = temp.right
            while succ.left:
                succ = succ.left

            temp.data = succ.data
            temp.right = self.delete(temp.right, succ.data)

        return temp

    # Preorder
    def preorder(self, temp):
        if temp:
            print(temp.data, end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)

    # Postorder
    def postorder(self, temp):
        if temp:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data, end=" ")


# Main Program
b = BST()

# Insert Product IDs
arr = [150, 100, 200, 75, 125, 175, 250, 60, 90, 110]

for i in arr:
    b.insert(Node(i))

# Ascending Order
print("Ascending Order:")
b.inorder(b.root)

# Search
print("\nSearch Product ID 175:")
if b.search(175):
    print("Product Found")
else:
    print("Product Not Found")

# Delete 100
print("\nAfter Deleting 100:")
b.root = b.delete(b.root, 100)
b.inorder(b.root)

# Preorder
print("\nPreorder:")
b.preorder(b.root)

# Postorder
print("\nPostorder:")
b.postorder(b.root)

# Min and Max
print("\nMinimum:", b.minimum(b.root))
print("Maximum:", b.maximum(b.root))

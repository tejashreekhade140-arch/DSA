
# E-Commerce Product Search System using BST

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 1. Insert Product ID
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    temp = temp.left

            elif new_node.data > temp.data:
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right
            else:
                print("Duplicate Product ID:", new_node.data)
                return

    # 2. Display Product IDs in Ascending Order
    def inorder(self, temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)

    # 3. Search Product ID
    def search(self, key):
        temp = self.root

        while temp is not None:
            if key == temp.data:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        return False

    # Find Minimum Node
    def minimum(self, temp):
        while temp.left is not None:
            temp = temp.left
        return temp

    # Find Maximum Node
    def maximum(self, temp):
        while temp.right is not None:
            temp = temp.right
        return temp

    # Find Inorder Successor
    def successor(self, temp):
        return self.minimum(temp.right)

    # 4. Delete Product ID using Inorder Successor
    def delete(self, temp, key):

        if temp is None:
            return None

        if key < temp.data:
            temp.left = self.delete(temp.left, key)

        elif key > temp.data:
            temp.right = self.delete(temp.right, key)

        else:
            # Case 1: No child
            if temp.left is None and temp.right is None:
                return None

            # Case 2: Only right child
            elif temp.left is None:
                return temp.right

            # Case 3: Only left child
            elif temp.right is None:
                return temp.left

            # Case 4: Two children
            else:
                succ = self.successor(temp)
                temp.data = succ.data
                temp.right = self.delete(temp.right, succ.data)

        return temp

    # 5. Preorder Traversal
    def preorder(self, temp):
        if temp is not None:
            print(temp.data, end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)

    # 5. Postorder Traversal
    def postorder(self, temp):
        if temp is not None:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data, end=" ")


# Main Program

b = BST()

# Insert Product IDs
product_ids = [150, 100, 200, 75, 125, 175, 250, 60, 90, 110]

for value in product_ids:
    b.insert(Node(value))

# Display in Ascending Order
print("Product IDs in Ascending Order:")
b.inorder(b.root)

# Search Product ID
key = 175

print("\n\nSearching Product ID:", key)

if b.search(key):
    print("Product ID Found")
else:
    print("Product ID Not Found")

# Delete Product ID 100
print("\nDeleting Product ID: 100")

b.root = b.delete(b.root, 100)

print("Product IDs after Deletion:")
b.inorder(b.root)

# Preorder Traversal
print("\n\nPreorder Traversal:")
b.preorder(b.root)

# Postorder Traversal
print("\n\nPostorder Traversal:")
b.postorder(b.root)

# Minimum Product ID
print("\n\nMinimum Product ID:", b.minimum(b.root).data)

# Maximum Product ID
print("Maximum Product ID:", b.maximum(b.root).data)

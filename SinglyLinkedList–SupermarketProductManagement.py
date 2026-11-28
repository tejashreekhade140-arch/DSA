
class Node:
    def __init__(self, pid, name, qty, price):
        self.pid = pid
        self.name = name
        self.qty = qty
        self.price = price
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Add new product
    def add_product(self, pid, name, qty, price):
        new_node = Node(pid, name, qty, price)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

        print("Product added successfully!")

    # 2. Search product using ID
    def search_product(self, pid):
        temp = self.head

        while temp is not None:
            if temp.pid == pid:
                print("Product Found!")
                print(temp.pid, temp.name,
                      temp.qty, temp.price)
                return
            temp = temp.next

        print("Product not found!")

    # 3. Update product quantity
    def update_quantity(self, pid, qty):
        temp = self.head

        while temp is not None:
            if temp.pid == pid:
                temp.qty = qty
                print("Quantity updated!")
                return
            temp = temp.next

        print("Product not found!")

    # 4. Delete product
    def delete_product(self, pid):
        temp = self.head
        prev = None

        while temp is not None:
            if temp.pid == pid:

                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                print("Product deleted!")
                return

            prev = temp
            temp = temp.next

        print("Product not found!")

    # 5. Display all products
    def display(self):
        temp = self.head

        if temp is None:
            print("No products available!")
            return

        while temp is not None:
            print(temp.pid, temp.name,
                  temp.qty, temp.price)
            temp = temp.next

    # 6. Find highest price
    def highest_price(self):
        if self.head is None:
            print("No products available!")
            return

        temp = self.head
        highest = temp

        while temp is not None:
            if temp.price > highest.price:
                highest = temp
            temp = temp.next

        print("Highest Price Product:")
        print(highest.name, highest.price)

    # 7. Products below quantity limit
    def low_quantity(self, limit):
        temp = self.head

        while temp is not None:
            if temp.qty < limit:
                print(temp.name, temp.qty)
            temp = temp.next


# Main program
ll = LinkedList()

ll.add_product(101, "Laptop", 10, 50000)
ll.add_product(102, "Mouse", 5, 500)
ll.add_product(103, "Keyboard", 15, 1000)

print("\nAll Products:")
ll.display()

print("\nSearch Product:")
ll.search_product(102)

print("\nUpdate Quantity:")
ll.update_quantity(102, 20)

print("\nDelete Product:")
ll.delete_product(103)

print("\nAfter Deletion:")
ll.display()

print("\nHighest Price:")
ll.highest_price()

print("\nProducts Below Quantity 12:")
ll.low_quantity(12)

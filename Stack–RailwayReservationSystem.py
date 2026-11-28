
class Stack:
    def __init__(self):
        self.tickets = []

    # 1. Push ticket
    def push(self, ticket_id):
        self.tickets.append(ticket_id)
        print("Ticket booked successfully!")

    # 2. Display tickets
    def display(self):
        if len(self.tickets) == 0:
            print("No booked tickets!")
        else:
            print("Booked Tickets:", self.tickets)

    # 3. Cancel latest ticket
    def pop(self):
        if len(self.tickets) == 0:
            print("Stack is empty!")
        else:
            cancelled = self.tickets.pop()
            print("Ticket cancelled:", cancelled)

    # 4. Display cancelled ticket
    def display_cancelled(self):
        if len(self.tickets) == 0:
            print("No cancelled ticket stored!")
        else:
            print("Latest booked ticket:", self.tickets[-1])

    # 5. Search ticket
    def search(self, ticket_id):
        if ticket_id in self.tickets:
            print("Ticket found!")
        else:
            print("Ticket not found!")

    # 6. Count tickets
    def count(self):
        print("Total booked tickets:",
              len(self.tickets))


# Main program
s = Stack()

s.push(101)
s.push(102)
s.push(103)

print("\nAll Tickets:")
s.display()

print("\nCancel Ticket:")
s.pop()

print("\nRemaining Tickets:")
s.display()

print("\nDisplay Top Ticket:")
s.display_cancelled()

print("\nSearch Ticket:")
s.search(102)

print("\nTotal Tickets:")
s.count()

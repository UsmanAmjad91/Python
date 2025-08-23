class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            print("Head Node created: " + new_node.value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print("Appended new Node with value: " + new_node.value)

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            print("Head Node created: " + new_node.value)
        else:
            new_node.next = self.head
            self.head = new_node
            print("Prepended new Head Node with value: " + new_node.value)
            print("Node following Head is: " + new_node.next.value)

# Testing
llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")

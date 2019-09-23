class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

class DoublyNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.prev = None

class LinkedList():
    
    def __init__(self, list_values):
        self.head = Node(list_values[0])
        curr = self.head
        for value in list_values[1:]:
            curr.next = Node(value)
            curr = curr.next 

    def append(self, value):
        curr = self.head
        while curr != None:
            curr = curr.next
        curr.next = Node(value)

    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.value)
            curr = curr.next

class DoublyLinkedList():

    def __init__(self, list_values):
        self.head = DoublyNode(list_values[0])
        curr = self.head
        for value in list_values[1:]:
            curr.next = DoublyNode(value)
            curr.next.prev = curr
            curr = curr.next 

    def append(self, value):
        curr = self.head
        while curr != None:
            curr = curr.next
        curr.next = Node(value)
        curr.next.prev = curr

    def printList(self):
        curr = self.head
        while curr != None:
            print(curr.value)
            curr = curr.next

    def printListReverse(self):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        while curr != None:
            print(curr.value)
            curr = curr.prev

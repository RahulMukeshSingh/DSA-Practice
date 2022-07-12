class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next =  node

    def print_data(self):
        current = self.head
        output = ""
        while(current):
           output += f'{current.data} '
           current = current.next
        print(output.strip())

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.print_data()

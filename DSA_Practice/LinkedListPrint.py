class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = node

    def print_even_div_by_3(self):
        current = self.head
        output = ''
        while(current):
            if current.data % 6 == 0:
                output += f'{current.data} '
            current = current.next
        output = output.strip()
        if not output: output = 'No found!'    
        print(output)
            
ll = LinkedList()
for i in range(1,19,4):
    ll.insert(i)
ll.print_even_div_by_3() 



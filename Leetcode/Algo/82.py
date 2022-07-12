class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    node = head
    prev = None
    while node:
        temp = node
        flag = False
        while(temp.next and temp.val == temp.next.val):
            temp = temp.next
            flag = True
        if flag:
            if not prev:
                head = temp.next
                node = head
                continue
            else: 
                prev.next = temp.next
                node = prev
        prev = node
        node = node.next    
    return head        
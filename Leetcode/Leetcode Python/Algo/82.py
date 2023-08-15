class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    prev = None
    curr = head
    count = 0
    prev_distinct = None
    while curr:
        if not prev or curr.val != prev.val:
            if count == 2:
                if prev_distinct: prev_distinct.next = curr
                else: head = curr
            elif count == 1: prev_distinct = prev
            count = 1
        else:
            count = 2 
        prev  = curr       
        curr = curr.next
    if count == 2:
        if prev_distinct: prev_distinct.next = None
        else: head = None
    return head



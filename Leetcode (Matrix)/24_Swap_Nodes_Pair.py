# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode(0, head)
        prev, current = temp, head

        while current and current.next:
            next_to_next_node  = current.next.next
            next_node = current.next

            next_node.next = current
            current.next = next_to_next_node
            prev.next = next_node
            prev = current
            current = next_to_next_node

        return temp.next
        
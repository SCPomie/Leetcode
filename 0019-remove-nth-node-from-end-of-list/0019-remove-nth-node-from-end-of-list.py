# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #sets the dummy
        dummy = ListNode(0, head)
        #initialise the left and right
        left, right = dummy, head
        
        #move right n nodes
        while n > 0:
            right = right.next
            n -= 1
        
        #move both until right reaches the end
        #left will stop one node before the node to remove
        while right:
            right = right.next
            left = left.next
        #skip the target node
        left.next = left.next.next

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #initialise fast and slow pointer at the start
        fast, slow = head, head
        #while fast and the fast next pointer exists
        while fast is not None and fast.next is not None:
            #slow pointer increment by 1 while fast increment by 2
            slow = slow.next
            fast = fast.next.next
            #if they ever meet then its a cycle return True
            if slow == fast:
                return True
        return False
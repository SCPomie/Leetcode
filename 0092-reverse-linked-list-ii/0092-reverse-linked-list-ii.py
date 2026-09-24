# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        #traverse the linked list until left
        for _ in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        #reverse the linked list
        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext
        #reconnect the pointers using cur and prev
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next
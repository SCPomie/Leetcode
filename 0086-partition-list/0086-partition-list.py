# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummyBig = ListNode(0)
        dummySmall = ListNode(0)
        dummybb = dummyBig
        dummyss = dummySmall

        cur = head
        while cur:
            if cur.val >= x:
                dummyBig.next = cur
                dummyBig = dummyBig.next
            else:
                dummySmall.next = cur
                dummySmall = dummySmall.next
            cur = cur.next
        
        dummySmall.next = dummybb.next
        dummyBig.next = None

        return dummyss.next
        
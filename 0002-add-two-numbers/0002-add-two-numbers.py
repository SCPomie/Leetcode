# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans_list = ListNode()
        dummy = ans_list
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            total = carry + x + x2
            digit = total % 10
            carry = total // 10
            ans_list.val = digit
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or carry:
                ans_list.next = ListNode()
                ans_list = ans_list.next
        return dummy
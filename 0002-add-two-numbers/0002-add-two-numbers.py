# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0

        while l1 or l2 or carry:
            #gets the l1 and l2 value if they exists otherwise 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            #calculates the value and the carry 
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            #add the cur.next value
            cur.next = ListNode(val)
            # move the pointer to the next
            cur = cur.next
            #move the l1 and l2 to the next one if they exists otherwise mark them as None
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        #return the dummy next 
        return dummy.next
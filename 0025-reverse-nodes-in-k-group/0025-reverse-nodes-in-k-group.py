# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            #finds the kth node
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            #the first node after the kth node
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            #reversing the linked list
            while curr != groupNext:

                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            #saves the old group head(becomes the tail after reversal)
            tmp = groupPrev.next
            #connect previous group to new group head
            groupPrev.next = kth
            #move group pre to the tail of the reversed group
            groupPrev = tmp
        return dummy.next
    
    #function used to determin the group size k
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
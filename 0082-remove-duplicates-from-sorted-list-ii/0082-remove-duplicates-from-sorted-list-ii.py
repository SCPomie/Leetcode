# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        #create the dummy node
        dummy = ListNode(0, head)
        #set up the two pointers
        prev, curr = dummy, head
        #while the curr nodes exists
        while curr:
            #if the value of the curr node is equal to the curr.next.val
            if curr.next and curr.val == curr.next.val:
                #enter a loop incrementing curr till the last duplicate
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                #set prev.next to cur.next to remove all duplicates
                prev.next = curr.next
            #if it is unique just increment prev
            else:
                prev = prev.next
            #increment curr.next as normal
            curr = curr.next
        
        return dummy.next
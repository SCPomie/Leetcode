# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        #gets the length and the final Node in the linked list
        length, tail = self.findLength(head) 

        if not head:
            return head
        #gets the k element, useful when k is bigger than the length, as its the same thing as just % the length
        k = k % length 

        #base condition, if k == 0, do nothing just return
        if k == 0:
            return head
        #sets the dummy element and the new Tail to dummy
        dummy = ListNode(0, head)
        newTail = dummy

        #loops over the linked list til the new tail Node
        for _ in range(length - k):
            newTail = newTail.next
        
        #sets the new Head. the New Head would be the New Tail.next as the newTail will be the last Node in the linked list
        newHead = newTail.next
        #the old tail.next pointer will then point to the head 
        tail.next = head
        #set the newTail.next to None to break the cycle
        newTail.next = None
        #return the linked list with the newHead
        return newHead

    #gets the last node and the length of the linked list
    def findLength(self, head):
        length = 0
        tail = None

        while head:
            tail = head
            head = head.next
            length += 1

        return length, tail
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creates a new linked list
        ans = ListNode()
        cur = ans
        # a while loop going over the two linked list until one of them are empty
        while (list1 != None and list2 != None):
            # connects the linked list value to the newly generated linked list
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            #sets cur to cur.next moving the linked list
            cur = cur.next
        #sets the next of cur to one of the remaining linked list
        cur.next = list1 or list2
        #return ans.next because ans is just a dummy
        return ans.next
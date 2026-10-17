# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #base case
        if not lists or len(lists) == 0:
            return None
        #while loop only stopping when the length is smaller than 1
        while len(lists) > 1:
            #creates a new list
            mergedLists = []
            #iterates through the linked list by 2 at a time
            for i in range(0, len(lists), 2):
                #gets list 1 and list 2
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                #merge the two linked lists and append into the mergedLists
                mergedLists.append(self.mergeList(l1, l2))
            #update the lists to be mergedLists
            lists = mergedLists
        return lists[0]
    
    #helper function to merge two lists together
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
            
        return dummy.next
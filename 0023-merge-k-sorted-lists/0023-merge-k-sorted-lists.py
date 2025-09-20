# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        dummy = ans
        list_val = []

        for i in range(len(lists)):
            while lists[i]:
                list_val.append(lists[i].val)
                lists[i] = lists[i].next
        if len(list_val) == 0:
            return None

        list_val.sort()  
        for i, ch in enumerate(list_val):
            ans.val = ch
            if i <= len(list_val) - 2:
                node = ListNode()
                ans.next = node
                ans = ans.next
        return dummy
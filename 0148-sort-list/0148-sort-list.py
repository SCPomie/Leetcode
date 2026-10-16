class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        #base case if the list is empty or has one node
        if not head or not head.next:
            return head

        #initialise fast and slow pointers to divide the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #gets the left and right pointers
        right = slow.next
        left = head

        #disconnect the two halves
        slow.next = None

        #recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        #initialise dummy and tail for merging
        dummy = ListNode()
        tail = dummy

        #merge the two sorted linked lists
        while left and right:
            if left.val <= right.val:
                #attach the left node
                tail.next = left
                left = left.next
            else:
                #attach the right node
                tail.next = right
                right = right.next

            #move tail to the last attached node
            tail = tail.next

        #attach the remaining nodes
        tail.next = left if left else right

        #return the head of the sorted list
        return dummy.next

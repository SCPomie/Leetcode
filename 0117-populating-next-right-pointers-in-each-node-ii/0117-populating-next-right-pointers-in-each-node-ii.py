"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # First node of the current level
        cur = root

        while cur:
            # Dummy node acts as a temporary starting point
            # for the next level
            dummy = Node(0)
            tail = dummy

            # Traverse the current level using the next pointers
            while cur:

                # Add the left child to the next level
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next

                # Add the right child to the next level
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next

                # Move horizontally across the current level
                cur = cur.next

            # dummy.next is the first node of the next level
            cur = dummy.next

        return root
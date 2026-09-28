"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #return None if no inputs
        if not root:
            return None

        #initialise the queue
        queue = deque([root])
        #while queue still exists
        while queue:
            #gets the level that you are in
            level_size = len(queue)
            #initalise prev to none
            prev = None
            #for iterate through the first level
            for i in range(level_size):
                #pop the element at the left
                node = queue.popleft()
                #if prev exists, set the prenode.next to the current node
                if prev:
                    prev.next = node
                #if node.left/right exists, append them to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                #sets prev to the current node before next iteration
                prev = node
        #returns the root
        return root
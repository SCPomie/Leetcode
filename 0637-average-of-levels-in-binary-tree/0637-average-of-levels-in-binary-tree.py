# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        #base case
        if not root:
            return []

        #initialise the answer and the queue
        result, queue = [], deque([root])

        #while the queue exists
        while queue:
            #length of the queue
            queue_length = len(queue)
            level_sum = 0

            #loops through the queue
            for i in range(queue_length):
                node = queue.popleft()

                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / queue_length)

        return result
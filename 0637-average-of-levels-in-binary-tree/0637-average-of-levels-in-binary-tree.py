# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        #base case
        if not root:
            return []

        #initialise the answer and the queue
        result, queue = [], [root]
        average = 0
        #while the queue exists
        while queue:
            #length of the queue:
            queue_length = len(queue)
            #loops through the queue
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    average += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average = average / queue_length
            result.append(average)
            average = 0
        return result
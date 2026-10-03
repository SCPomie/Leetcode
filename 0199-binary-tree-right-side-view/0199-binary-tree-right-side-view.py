# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        #base case it not root just return empty
        if not root:
            return []
        #initialise the result and the queue
        result, queue = [], [root]
        #while the queue is there
        while queue:
            #add the last element in the queue to the result
            #last element in the queue is always the right value
            result.append(queue[-1].val)
            #a for loop going over the tree with BFS
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        #return the result
        return result
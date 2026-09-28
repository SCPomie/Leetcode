# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base condition
        if not root:
            return 0
        #gets the max of each side
        depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
        #adds the count
        return depth + 1

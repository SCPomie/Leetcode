# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        #checks for base case, e.g, not a node
        if not root:
            return False
        #decrease the target as you go down
        targetSum -= root.val
        #if its a leaf node, then check if it equals to targetSum
        if not root.left and not root.right:
            return targetSum == 0
        #if not a leafNode, recursively go down
        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)

        return left or right
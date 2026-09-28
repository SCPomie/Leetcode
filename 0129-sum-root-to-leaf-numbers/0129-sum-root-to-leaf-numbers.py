# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(root, string):
            #base case to stop when node is None
            if not root:
                return 0
            #add the val of the current node
            string += str(root.val)
            #if you are at the leaf, return the int value of the current string
            if not root.left and not root.right:
                return int(string)
            #recursive go down the tree, left first then right
            left, right = dfs(root.left, string), dfs(root.right, string)
            #return the added value
            return left + right
        
        return dfs(root, "")
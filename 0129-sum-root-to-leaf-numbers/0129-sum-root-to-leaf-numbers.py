# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(root, string):
            if not root:
                return 0
            
            string += str(root.val)

            if not root.left and not root.right:
                return int(string)
            
            left, right = dfs(root.left, string), dfs(root.right, string)

            return left + right
        
        return dfs(root, "")
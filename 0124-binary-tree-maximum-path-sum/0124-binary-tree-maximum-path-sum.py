# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(root):
            #base case
            if not root:
                return 0
            #goes left and right node to check for the maximum sum
            left = dfs(root.left)
            right = dfs(root.right)
            #skipps out the negative number
            left_max = max(left, 0)
            right_max = max(right, 0)
            #checks if the split happens, if the  sum of the split is greater than the current ans
            self.ans = max(self.ans, (root.val + left_max + right_max))
            #return the value to it's parent so parent gets its value and the max of its child
            return root.val + max(left_max, right_max)
        dfs(root)
        return self.ans
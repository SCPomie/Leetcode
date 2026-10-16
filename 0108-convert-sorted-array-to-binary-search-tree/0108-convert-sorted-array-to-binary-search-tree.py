# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        
        #dfs recursion
        def dfs(left, right):
            #base case, when there is no element left
            if left > right:
                return None
            #gets the mid
            mid = (left + right) // 2
            #create the node
            node = TreeNode(nums[mid])
            #recursive built the left and the right nodes
            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)

            #return the root
            return node
        
        return dfs(0, len(nums) - 1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            #if statement to check if the nodes matches
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            #recursively goes through the left and the right nodes of the tree
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            #returns tree if they match
            return (left and right)
        #recursive dfs function to return if its the same tree or not
        return dfs(p, q)
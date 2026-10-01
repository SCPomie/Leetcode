# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #base case not root
        if not root:
            return None
        
        # if the node is equal to p or q return it
        if root == p or root == q:
            return root
        
        #recursively go through the tree 
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        #if l and r all exists, return that function
        if l and r:
            return root
        
        #if only 1 is returned, then return that one
        else:
            return l or r
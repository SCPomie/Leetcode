# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case, if root is none return None
        if not root:
            return None
        #swaps the children nodes
        tmp = root.right
        root.right = root.left
        root.left = tmp
        #recursive calls on the Tree nodes
        self.invertTree(root.left)
        self.invertTree(root.right)
        #return the roots
        return root
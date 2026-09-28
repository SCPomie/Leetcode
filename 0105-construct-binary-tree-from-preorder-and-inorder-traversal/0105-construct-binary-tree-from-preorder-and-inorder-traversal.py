# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #base condition if the inputs are empty return None
        if not preorder or not inorder:
            return None
        #gets the root
        root = TreeNode(preorder[0])
        #gets the index of the root in the inorder
        mid = inorder.index(preorder[0])
        #recursive built the left side, and the right side using the properties of inorder and preorder traversal
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1:])
        return root

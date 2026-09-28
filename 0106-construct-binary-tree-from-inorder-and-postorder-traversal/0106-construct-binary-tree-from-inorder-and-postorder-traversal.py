# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder or not postorder:
            return None
        
        #gets the root
        root = TreeNode(postorder[-1])
        #gets the mid of the inorder of the original root
        mid = inorder.index(postorder[-1])
        #build the tree recursively using the properties of inorder and postorder traversal
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid: -1])
        
        return root
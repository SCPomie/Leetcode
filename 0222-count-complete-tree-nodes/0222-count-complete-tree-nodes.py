# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode | None) -> int:

        # Base case: an empty tree contains 0 nodes
        if not root:
            return 0

        # Get the height of a subtree by following
        # the leftmost path
        def getHeight(node):
            height = 0

            while node:
                height += 1
                node = node.left

            return height

        # Find the heights of the left and right subtrees
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)

        if leftHeight == rightHeight:
            # If both heights are equal, the LEFT subtree is perfect.

            return (2 ** leftHeight) + self.countNodes(root.right)

        else:
            # If leftHeight > rightHeight, the RIGHT subtree is perfect.
            return (2 ** rightHeight) + self.countNodes(root.left)
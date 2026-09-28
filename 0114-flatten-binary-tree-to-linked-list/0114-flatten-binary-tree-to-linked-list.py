# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Flattens the subtree starting at root
        # and returns the tail (last node) of the flattened subtree.
        def dfs(root):

            # Base case: empty subtree has no tail.
            if not root:
                return None

            # Recursively flatten the left and right subtrees.
            # Keep their tails so we know where each flattened subtree ends.
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            # If there is a left subtree, it needs to be moved
            # between the current root and the right subtree.
            if root.left:

                # Connect the end of the flattened left subtree
                # to the beginning of the flattened right subtree.
                leftTail.right = root.right

                # Move the flattened left subtree to the right.
                root.right = root.left

                # A flattened tree should have no left children.
                root.left = None

            # The tail of the flattened tree is:
            # 1. rightTail, if a right subtree exists
            # 2. otherwise leftTail, if a left subtree exists
            # 3. otherwise root itself, if root is a leaf
            last = rightTail or leftTail or root

            return last

        dfs(root)
        
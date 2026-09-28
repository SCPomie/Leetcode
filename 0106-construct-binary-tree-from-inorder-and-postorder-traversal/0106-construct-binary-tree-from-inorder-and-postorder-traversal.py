# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Store each value's index in inorder.
        # This lets us find the root's position in O(1)
        # instead of using inorder.index(), which takes O(n).
        inorderIdx = {value: i for i, value in enumerate(inorder)}

        # l and r represent the section of the original inorder list
        # that the current recursive call is responsible for.
        # This avoids creating new lists with slicing.
        def dfs(l, r):

            # If the boundaries cross, there are no nodes
            # left in this subtree.
            if l > r:
                return None

            # Postorder is: [left, right, root].
            # Therefore, the last element is the current root.
            # pop() gets the root and removes it from postorder.
            root = TreeNode(postorder.pop())

            # Find where the root appears in inorder.
            # Inorder is: [left subtree, root, right subtree].
            idx = inorderIdx[root.val]

            # Since we are consuming postorder backwards, its order is:
            # [root, right, left].
            # Therefore, we MUST build the right subtree first.
            #
            # idx + 1 to r represents the right portion of inorder.
            root.right = dfs(idx + 1, r)

            # l to idx - 1 represents the left portion of inorder.
            root.left = dfs(l, idx - 1)

            # Return the completed subtree rooted at this node.
            return root

        # Initially, the entire inorder list belongs to the tree.
        return dfs(0, len(inorder) - 1)
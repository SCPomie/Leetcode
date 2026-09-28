# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        #DFS recursive function
        def dfs(left, right):
            #if two nodes are none they are true
            if not left and not right:
                return True
            #if one node and another node is None then false
            if not left or not right:
                return False
            #return True if the val are the same and also recursive calls the tree
            return (left.val == right.val and 
                    dfs(left.left, right.right) and
                    dfs(left.right, right.left)
                    )
        
        return dfs(root.left, root.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #initialise the prev and the answer variable
        prev = None
        answer = float("inf")

        def inorder(node):
            nonlocal prev, answer
            #base case
            if not node:
                return

            #go left
            inorder(node.left)

            #process current node
            if prev is not None:
                answer = min(answer, node.val - prev)

            prev = node.val

            #go right
            inorder(node.right)

        inorder(root)

        return answer
                    

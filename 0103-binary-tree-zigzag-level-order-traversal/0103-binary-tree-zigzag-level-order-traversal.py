# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        #base case
        if not root:
            return []
        
        #initialise the answer and the queue
        answer, q = [], deque([root])
        zig = 0

        #while the queue exists:
        while q:
            #iterates through the queue
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #check if we want to zig-zag
            if zig == 1:
                level.reverse()
            #revert the zig so that it follows the zig-zag pattern
            zig = 1 - zig
            answer.append(level)
        
        return answer
        
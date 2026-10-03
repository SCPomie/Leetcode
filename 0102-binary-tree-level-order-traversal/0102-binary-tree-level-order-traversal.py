# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Base case
        if not root:
            return []
        #initialise the answer and the queue
        ans = []
        q = deque([root])
        #while the queue exists
        while q:
            #counts the level
            level = []
            #iterates through the queue, pop the element and add the values
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            #if level contains any value, add it to the answer
            if level:
                ans.append(level)
        #return the answer
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #initialise the stack and the quque
        ans = []
        q = deque([root])
        #while the queue exists
        while q:
            rightSide = None
            #loop through the queue
            for i in range(len(q)):
                #pop the elements
                node = q.popleft()
                #if it's a node, set the rightside = Node and then append the left and the right values
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            #if rightside is valid, append it to answer
            if rightSide:
                ans.append(rightSide.val)
        return ans

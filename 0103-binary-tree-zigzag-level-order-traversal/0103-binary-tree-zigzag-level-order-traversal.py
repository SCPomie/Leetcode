# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        #base case
        if not root: return []
        #start the quque, result and the flip variable for zig-zag
        queue = deque([root])
        result = []
        flip = True
        #while a queue exists
        while queue:
            #gets the queue_len, level and revert the flip
            queue_len = len(queue)
            level = []
            flip = not flip
            #iterates through the current queue
            for i in range(queue_len):
                #if flip is true, pop the end of the queue and do the bfs with rigth -> left
                #else pop from the left and do the bfs normally left -> right
                if flip:
                    cur = queue.pop()
                    if cur.right:
                        queue.appendleft(cur.right)
                    if cur.left:
                        queue.appendleft(cur.left)
                else:
                    cur = queue.popleft()
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                #add the values
                level.append(cur.val)
            #append the level answer to the answer
            result.append(level)
        return result
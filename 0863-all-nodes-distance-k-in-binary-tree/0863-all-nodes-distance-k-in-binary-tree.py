# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #gets the dfs to get all the parents of each node collected
        parent = {}

        def dfs(node, par):
            if not node:
                return

            parent[node] = par

            dfs(node.left, node)
            dfs(node.right, node)
        #calls the bfs
        dfs(root, None)
        #initialise the queue, visited, and distance
        queue = deque([target])
        visited = {target}
        distance = 0

        #while the queue is not empty
        while queue:
            #base base, if the distance == k, then return all the nodes in the queue
            if distance == k:
                return [node.val for node in queue]
            #iterates through the queue
            for _ in range(len(queue)):
                #pops the leftmost element
                node = queue.popleft()
                #check the neighbours in the left, right and parent side
                for neighbor in (node.left, node.right, parent[node]):
                    #if neightbor exists and it is not in visited
                    if neighbor and neighbor not in visited:
                        #add the neighbor to visited and the queue
                        visited.add(neighbor)
                        queue.append(neighbor)
            #increment the stance
            distance += 1
    
        return []

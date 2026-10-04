"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Hashmaps to store the copies
        oldtoNew = {}

        def dfs(node):
            #if the node is in the hashmap return the corresponding new copy of the node
            if node in oldtoNew:
                return oldtoNew[node]
            #create the new copy
            copy = Node(node.val)
            #add it to the hashmap using the old Node as the key
            oldtoNew[node] = copy
            #iterates through the neighbors in the old copy
            for nei in node.neighbors:
                #add the neighbours to the copy
                copy.neighbors.append(dfs(nei))
            #return the copy
            return copy
        #return the answer
        return dfs(node) if node else None

            
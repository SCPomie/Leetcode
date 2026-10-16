"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):
            #check if all values in the current square are the same
            allSame = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break

            #base case: return a leaf node if all values are the same
            if allSame:
                return Node(grid[r][c], True)

            #divide the square into four smaller squares
            n = n // 2

            #recursively construct the four quadrants
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            #return a parent node connected to the four children
            return Node(
                0, False,
                topLeft, topRight,
                bottomLeft, bottomRight
            )

        #start with the entire grid
        return dfs(len(grid), 0, 0)
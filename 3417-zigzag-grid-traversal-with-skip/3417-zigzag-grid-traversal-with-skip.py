class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        result = []
        count = 0

        row, col = len(grid), len(grid[-1])
        #iterates the first row
        for r in range(row):
            #iterates the columns
            for c in range(col):
                #if it's even row then positive left to right
                if r % 2 == 0:
                    index = c
                else:
                    #else go right to left
                    index = col - 1 - c
                #if count of is even then add it to the result
                if count % 2 == 0:
                    result.append(grid[r][index])
                
                count += 1
        return result

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #initialise the variables
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r,c):
            #initialise the queue and mark the grid with 0
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            #while the queu exists
            while q:
                #pops the queue
                row, col = q.popleft()
                #loops through vertial and horizontal directions
                for dr, dc in directions:
                    #add the vertical and horizontal directions to the popped row and cols in the queue
                    nr, nc = dr + row, dc + col
                    #checks the boundary and grid == 0, if any comes true skip it
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    #add the new position inside the grid to the queue. grid[nr][nc] == 1
                    q.append((nr, nc))
                    #mark that grid to 0, menaing visited
                    grid[nr][nc] = "0"


        #loop through the array, if you see 1, then use the bfs to iterate through it
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        
        return islands
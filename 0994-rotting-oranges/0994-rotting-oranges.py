class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[-1])

        queue = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))

        count = 0        
        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                # Down
                if r + 1 < row and grid[r + 1][c] == 1:
                    queue.append((r + 1, c))
                    grid[r + 1][c] = 2

                # Up
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    queue.append((r - 1, c))
                    grid[r - 1][c] = 2

                # Right
                if c + 1 < col and grid[r][c + 1] == 1:
                    queue.append((r, c + 1))
                    grid[r][c + 1] = 2

                # Left
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    queue.append((r, c - 1))
                    grid[r][c - 1] = 2
            
            if queue:
                count += 1

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1

        return count

        


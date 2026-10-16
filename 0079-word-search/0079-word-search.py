class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        #set up the row, col, visited set 
        row, col = len(board), len(board[0])

        visited = set()
        #back track
        def backtrack(r, c, i):
            #basecase if i is equal t the length of word return True
            if i == len(word):
                return True
            #boundary check and also checks for word and if current position is in visited
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[i] or (r, c) in visited:
                return False
            #add the current posistion to visit
            visited.add((r, c))
            #back track to find the word, return True if one of the case is true
            if  (backtrack(r + 1, c, i + 1) or   #down
                backtrack(r - 1, c, i + 1) or #up
                backtrack(r, c + 1, i + 1) or   #right
                backtrack(r, c - 1, i + 1) or #left
                visited.remove((r, c))):
                return True
        #loop over the board, return True if any cordinate will provide a good word
        for r in range(row):
            for c in range(col):
                if backtrack(r, c, 0):
                    return True
        return False

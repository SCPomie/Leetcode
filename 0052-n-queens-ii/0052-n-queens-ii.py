class Solution:
    def totalNQueens(self, n: int) -> int:
        #initialise the sets
        col = set()
        posDiag = set()
        negDiag = set()

        res = 0

        #backtracking
        def backtrack(r):
            nonlocal res
            #base condition
            if r == n:
                res += 1
                return

            #loops through the col
            for c in range(n):
                #skip these spots
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                #calls backtracking
                backtrack(r + 1)

                #removes the spots for backtracking
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        
        backtrack(0)
        return res
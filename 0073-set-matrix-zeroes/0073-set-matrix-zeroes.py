class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        #goes over the row
        for r in range(rows):
            #goes over the cols
            for c in range(cols):
                # if the place is 0, mark the first col
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    # mark the second onward rows 
                    if r > 0:
                        matrix[r][0] = 0
                    # sets the zeros for the first row
                    else:
                        rowZero = True
        
        # converts the rows and cols to zeros based on the first row and col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        #checks if we need to change first col to zero
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # checks if we need to change the first row to zero
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
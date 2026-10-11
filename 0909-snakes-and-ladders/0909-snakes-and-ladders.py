class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        length = len(board)

        board.reverse()
        #funtion to convert into to rows and cols
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]
        
        #initialise the queue
        q = deque()
        q.append([1, 0]) #starting position and number of steps
        visited = set()
        #bfs traversal
        while q:
            #gets the current square value and moves
            square, moves = q.popleft()
            #rolls the dice, 1 to 6 to get the value of the next few steps
            for i in range(1, 7):
                #gets the value of the next square
                nextSquare = square + i
                #convert the nextSquare into the corresponding cordinates
                r, c = intToPos(nextSquare)
                #if they encounter a ladder or snake, change the nextSquare to the destination of the ladder/snake
                if board[r][c]  != -1:
                    nextSquare = board[r][c]
                #checks if you reach the target location
                if nextSquare == length * length:
                    return moves + 1
                #if the new nodes are not visited then add them into visited and append into the queue
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1


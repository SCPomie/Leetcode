#set up the classes for a prefix tree
class TrieNode():

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #initialise the tree
        root = TrieNode()
        #add construct the prefix tree
        for w in words:
            root.addWord(w)
        #initialise the row, col, res and visit 
        row, col = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c , node, word):
            #base case of the dfs
            if (r < 0 or c < 0 or r >= row or c >= col or
             (r,c) in visit or board[r][c] not in node.children):
                return
            #add the visited node
            visit.add((r, c))
            #move onto the corresponding next node
            node = node.children[board[r][c]]
            #add the words
            word += board[r][c]
            #if the current node is a word add it to the result
            if node.isWord:
                res.add(word)
            #calls dfs on top, bottom, left and right of the board
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            #remove the visited node for back tracking
            visit.remove((r,c))
        
        #calls the dfs on every node on the board
        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")
        
        return list(res)

        
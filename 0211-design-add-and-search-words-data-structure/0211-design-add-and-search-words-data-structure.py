class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        #a dfs for the special . case
        def dfs(j, root):
            #set the cur as the root of the tree
            cur = root
            #iterate through the words with index 
            for i in range(j, len(word)):
                c = word[i]
                #if the index is .
                if c == ".":
                    #this line iterates through all the childs of the current node
                    for child in cur.children.values():
                        #calls the DFS on the next index character with the child of the current node
                        #if the dfs matches, return True indicating that there is a word
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            #makes sure that it is a word
            return cur.isWord
        return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
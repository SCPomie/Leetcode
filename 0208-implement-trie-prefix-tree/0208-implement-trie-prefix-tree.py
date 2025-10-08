class TreeNode:
    #defines the Tree datastructure needed
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    #initialise the root
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        #set cur at the start of the tree
        cur = self.root
        #iterate character in words
        for c in word:
            #if c not in the hash map, add it otherwise jump to the corresponding TreeNode
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        #Mark the end of the word
        cur.isEnd = True

    def search(self, word: str) -> bool:
        #set cur as the root of the tree
        cur = self.root
        #check if c is in the tree, if not return False else jump to the corresponding TreeNode
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        #return if the character is marked as the end of a word
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        #sets cur as the root of the tree
        cur = self.root
        #iterate through the prefix
        for c in prefix:
            #if c not in the tree then return False else jump to the corresponding treenode
            if c not in cur.children:
                return False
            cur = cur.children[c]
        #return True after every character is iterated
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
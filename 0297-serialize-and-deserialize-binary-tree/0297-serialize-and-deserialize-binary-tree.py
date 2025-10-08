# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        #res takes the order of the preorder of the tree
        res = []
        def dfs(node):
            #base case if not node, append N into res
            if not node:
                res.append("N")
                return 
            #adds the str value of the current node and then move to left subtree recrusively and then right recursively
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        #calls the dfs function and then return the result as a string
        dfs(root)
        return (",").join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #split the string, and set the index to 0
        data = data.split(",")
        self.index = 0
        def dfs():
            #base case, if currnet node is N then increment index and return none
            if data[self.index] == "N":
                self.index += 1
                return None
            #create the tree node and increment the index
            node = TreeNode(int(data[self.index]))
            self.index += 1
            #goes to the left tree recursively and then the right subtree recursively
            node.left = dfs()
            node.right = dfs()
            #return the root node
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
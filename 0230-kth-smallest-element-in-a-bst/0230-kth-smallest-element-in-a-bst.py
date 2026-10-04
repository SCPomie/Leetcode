class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #base case
        if not root:
            return None

        #initialise the counter, stack and current node
        n = 0
        stack = []
        curr = root

        #continue while there are nodes to explore or nodes waiting in the stack
        while curr or stack:

            #go as far left as possible, storing nodes to return to later
            while curr:
                stack.append(curr)
                curr = curr.left

            #pop the next smallest node from the stack
            curr = stack.pop()

            #increment the number of nodes processed
            n += 1

            #if this is the kth smallest node, return its value
            if n == k:
                return curr.val

            #move to the right subtree and repeat the inorder traversal
            curr = curr.right
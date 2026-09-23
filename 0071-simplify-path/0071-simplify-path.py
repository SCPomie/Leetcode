class Solution:
    def simplifyPath(self, path: str) -> str:
        
        #initialise a stack
        stack = []
        #split the paths
        path = path.split('/')
        #for characters in path
        for n in path:
            # if its currently empty or just a single dot, just ignore and carry to next iteration
            if n == '' or n == '.':
                continue
            # if it is .. then pop the stack else continue to next if stack is empty
            elif n == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            #append the stack
            else:
                stack.append(n)
        #joins the stack to get the final answer
        ans = ('/').join(stack)
        #return / + ans if stack exists otherwise just return a single /
        return "/"+ans if stack else "/"
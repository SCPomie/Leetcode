class Solution:
    def simplifyPath(self, path: str) -> str:
        
        #initialise a stack
        stack = []
        path = path.split('/')

        for n in path:
            if n == '' or n == '.':
                continue
            elif n == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(n)
        
        ans = ('/').join(stack)
        return "/"+ans if stack else "/"
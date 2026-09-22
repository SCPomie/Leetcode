class Solution:
    def isValid(self, s: str) -> bool:
        #sets up the stack and the hashmap
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        #goes through th strings
        for c in s:
            #if the current string is a closing bracket
            if c in closeToOpen:
                #if the stack exists and the last element in the stack is equal to the corresponding opening element in the hashmap
                if stack and stack[-1] == closeToOpen[c]:
                    #pop the stack
                    stack.pop()
                    #else if not equal then return False
                else:
                    return False
            else:
                #append the stack with the current character
                stack.append(c)
        #return true if stack is empty otherwise False
        return True if not stack else False
class MinStack:

    def __init__(self):
        #sets the normal and the get minimum stack
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        #add the value to the normal stack
        self.stack.append(value)
        #if the minstack is empty add the new value
        if not self.minStack:   
            self.minStack.append(value)
        #otehrwise add the minimum of the newest value and the current stack value at the top
        else:
            self.minStack.append(min(value, self.minStack[-1]))
    #pops the stack, both of the stack to keep them sychronised
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    #returns the top of the stack
    def top(self) -> int:
        return self.stack[-1]
    #gets the minimum value of the stack which is the top of the minStack
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
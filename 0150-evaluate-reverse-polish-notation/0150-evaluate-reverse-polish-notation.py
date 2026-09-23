import operator
class Solution(object):
    def evalRPN(self, tokens):
        #define the operators
        operators = {'+' : operator.add, 
                    '/'  : lambda a, b: int(a / b), 
                    '-'  : operator.sub,
                    '*'  : operator.mul
                    }
        #initialise the stack
        stack = []
        #for each element in the stack
        for n in tokens:
            #if the element is not an operator append it
            if n not in operators:
                stack.append(int(n))
            else:
                #otherwise append out the two numbers
                num1 = stack.pop()
                num2 = stack.pop()
                #gets the result by using the operators defined in the dictionary
                result = operators[n](num2, num1)
                #add the result back to the stacck
                stack.append(result)
        #return the answer
        return stack[0]

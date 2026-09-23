class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1
        #loops throught the inputs
        for c in s:
            #if it is a digit, calculate the number because the input is a string
            if c.isdigit():
                number = number * 10 + int(c)
            #if you encounter a non_number. The sign is changed after the calculation because the sign is for the next number
            elif c == "+":
                #add previous result to results with regards to the signs
                result += sign * number
                #reset the number and change the sign based on the sign
                number = 0
                sign = 1
            #same thing as the + case
            elif c == "-":
                result += sign * number
                number = 0
                sign = - 1
            #if you encounter the open (, add the result and sign to the stack and reset result and sign
            elif c == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1
            #if you encounter the ending ")"
            elif c == ")":
                #get the current result and reset number
                result += sign * number
                number = 0
                #pop out the previous result and sign
                previous_sign = stack.pop()
                previous_result = stack.pop()
                #calculate the results with prev_result + (prev_sign * result)
                result = previous_result + previous_sign * result
        #add the last number as the loop does not process the last numhber
        result += sign * number
        #return the result
        return result
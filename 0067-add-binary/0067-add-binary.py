class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        #revert the strings
        a = a[:: -1]
        b = b[:: - 1]
        #iterate through the max length of a or b
        for i in range(max(len(a), len(b))):
            #gets the digit, 0 if out of bound
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            #gets the total, the carry and the char
            total = digitA + digitB + carry
            char = str(total % 2)
            carry = total // 2
            #add the current result, the char to the final result
            res = char + res
        #if there is a carry after the loop then add 1 in the front of the result
        if carry:
            res = "1" + res
        #return result
        return res
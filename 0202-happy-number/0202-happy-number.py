class Solution:
    def isHappy(self, n: int) -> bool:
        #gets the set to record values
        visit = set()
        # a loop while n is not in visit
        while n not in visit:
            # add n to visit
            visit.add(n)
            # gets the new n value
            n = self.sumOfSquares(n)
            #if n is equal to 1, return True
            if n == 1:
                return True
        # when the loop stops it means that there is a duplicate number/cycle in the set, return False
        return False

    # helper function to determine the new n value
    def sumOfSquares(self, n: int) -> int:
        output = 0
        # while n exists
        while n:
            # gets the last digit
            digit = n % 10
            # squares the last digit
            digit = digit ** 2
            # add it to the output
            output += digit
            # gets the new n value
            n = n // 10
        return output
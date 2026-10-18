class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #starts the loop from right to left
        for i in range(len(digits) - 1, -1, -1):
            #if the digit is not 9 then increament it by 1 and return the list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            #if digit is equal to 9 then set it to 0
            else:
                digits[i] = 0
        #if all digit is 9 then add 1 to the start of the list
        return [1] + digits
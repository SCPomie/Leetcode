class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        # Keep removing rightmost bits until left and right are equal
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        # Shift the common prefix back to its original position
        # The removed bits become 0
        return left << shift
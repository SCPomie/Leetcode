class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                mleft, mright = 0, len(matrix[mid]) - 1
                while mleft <= mright:
                    mmid = (mleft + mright) // 2
                    if matrix[mid][mmid] == target:
                        return True
                    elif matrix[mid][mmid] >= target:
                        mright = mmid - 1
                    else:
                        mleft = mmid + 1
                return False
            elif matrix[mid][-1] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return False
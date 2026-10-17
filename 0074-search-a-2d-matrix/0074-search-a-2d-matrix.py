class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Initialise the left and right pointers for the rows
        left, right = 0, len(matrix) - 1

        # Binary search to find the correct row
        while left <= right:
            mid = (left + right) // 2

            # Check if the target is within the current row's range
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                # Initialise the left and right pointers for the columns
                mleft, mright = 0, len(matrix[mid]) - 1

                # Binary search within the selected row
                while mleft <= mright:
                    mmid = (mleft + mright) // 2

                    # Return True if the target is found
                    if matrix[mid][mmid] == target:
                        return True

                    # If the current element is greater, search the left half
                    elif matrix[mid][mmid] >= target:
                        mright = mmid - 1

                    # Otherwise search the right half
                    else:
                        mleft = mmid + 1

                # Target is not found within the row
                return False

            # If the target is greater than the row's last element, search lower rows
            elif matrix[mid][-1] <= target:
                left = mid + 1

            # Otherwise search upper rows
            else:
                right = mid - 1

        # Return False if the target is not found
        return False
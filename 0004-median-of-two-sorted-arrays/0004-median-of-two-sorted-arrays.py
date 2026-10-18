class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Initialise the arrays, total length and half
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Make sure A is the smaller array
        if len(B) < len(A):
            A, B = B, A

        # Initialise the left and right pointers
        l, r = 0, len(A) - 1

        while True:
            # Find the partition indices for both arrays
            i = (l + r) // 2
            j = half - i - 2

            # Get the left and right values of each partition
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            # If both partitions are correct, calculate the median
            if Aleft <= Bright and Bleft <= Aright:
                # If total is odd, return the smallest right value
                if total % 2:
                    return min(Aright, Bright)

                # Otherwise return the average of the two middle values
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # If Aleft is too large, move the partition left
            elif Aleft > Bright:
                r = i - 1

            # Otherwise move the partition right
            else:
                l = i + 1
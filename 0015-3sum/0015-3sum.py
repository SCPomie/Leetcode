class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            st, end = i + 1, len(nums) - 1
            while st < end:
                threesum = a + nums[st] + nums[end]
                if threesum > 0:
                    end -= 1
                elif threesum < 0:
                    st += 1
                else:
                    result.append([a, nums[st], nums[end]])
                    st += 1
                    end -= 1
                    while nums[st] == nums[st - 1] and st < end:
                        st += 1
                    while nums[end] == nums[end + 1] and st < end:
                        end -= 1
        return result

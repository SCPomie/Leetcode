class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #initialise the set and the longest variable
        num_set = set(nums)
        longest = 0
        #iterates through the lists
        for num in num_set:
            # check if there is consecutive smaller number int the list, if not then set the current to the current numnber and count to 1
            if num - 1 not in num_set:
                current = num
                count = 1
                # while a consecutive + 1 number exists in the lists, increment current and count
                while current + 1 in num_set:
                    current += 1
                    count += 1
                # gets the longest value using max
                longest = max(longest, count)

        return longest
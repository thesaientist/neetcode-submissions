class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count_ones = 0
        for i in range(len(nums)):
            count_ones = count_ones + 1 if nums[i] else 0
            max_ones = count_ones if count_ones > max_ones else max_ones
        return max_ones
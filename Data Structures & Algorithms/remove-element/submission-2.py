class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        n = len(nums)
        i = 0
        while l < n:
            if nums[l] != val:
                nums[i] = nums[l]
                i += 1
            l += 1
        nums = nums[:i]
        return i
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        n = len(nums)
        i = 0
        while l < n:
            while l < n and nums[l] == val:
                l += 1
            if l < n:
                nums[i] = nums[l]
                i += 1
                l += 1
            else:
                break
        nums = nums[:i]
        return i
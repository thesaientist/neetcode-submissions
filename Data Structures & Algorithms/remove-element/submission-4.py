class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = i = 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
                continue
            nums[j] = nums[i]
            i += 1
            j += 1
        return j
            
        
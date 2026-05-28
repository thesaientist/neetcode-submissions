class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # loop through the elements while keeping track of unique elements
        k = 1
        last_ele = nums[0]
        i = 1
        while i < len(nums):
            ele = nums[i]
            # since array are non-decreasing, if the current element in the array doesn't match
            # the last element then it's a new unique element
            if ele != last_ele:
                nums[k] = ele
                k += 1
                last_ele = ele
            i += 1
        nums = nums[:k]
        return k

        
                
        
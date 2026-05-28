class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        curr_max = arr[n-1]
        for i in range(n-2, -1, -1):
            last_max = curr_max
            curr_max = max(arr[i], curr_max)
            arr[i] = last_max
        arr[n-1] = -1
        return arr

        
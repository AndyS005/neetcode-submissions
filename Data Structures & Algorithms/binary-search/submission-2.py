class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1 
        while first <= last:
            curr = first + ((last - first) // 2)
            if nums[curr] == target:
                return curr
            elif nums[curr] > target:
                last = curr - 1
            else:
                first = curr + 1
        
        return -1

        
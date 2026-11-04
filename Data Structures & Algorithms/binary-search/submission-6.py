class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums)
        while first < last:
            curr = first + ((last - first) // 2)
            if nums[curr] == target:
                return curr
            elif nums[curr] < target:
                first = curr + 1
            else:
                last = curr
            
        return -1
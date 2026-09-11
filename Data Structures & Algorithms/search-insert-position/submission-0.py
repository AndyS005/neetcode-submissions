class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        res = 0
        while first <= last:
            curr = first + ((last - first) // 2)
            if target > nums[last]:
                return last + 1
            if nums[curr] == target:
                return curr
            elif nums[curr] < target:
                first+=1 
            else:
                last-=1

        return last + 1
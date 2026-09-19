class Solution:
    def findMin(self, nums: List[int]) -> int:

        mini = nums[0]
        first, last = 0, len(nums) -1
        while first < last:
            curr = first + ((last - first) // 2)
            if nums[curr] > nums[last]:
                first = curr + 1
            else:
                last = curr
        return nums[first]

        
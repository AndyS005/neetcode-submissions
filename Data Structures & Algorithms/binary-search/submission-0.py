class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) -1
        while first <= last:
            curr = first + (last - first) // 2
            print(curr)
            if nums[curr] == target:
                return curr
            elif nums[curr] > target:
                last = curr - 1
            elif nums[curr] < target:
                first = curr + 1

        return -1

        
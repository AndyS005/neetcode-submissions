class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        at_index = {}
        for i, v in enumerate(nums):
            difference = target - v
            if difference in at_index:
                return [at_index[difference], i]
            at_index[v] = i
            



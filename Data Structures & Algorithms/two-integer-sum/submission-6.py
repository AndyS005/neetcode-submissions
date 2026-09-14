class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        at_index = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in at_index:
                return [at_index[difference], index]
            at_index[value] = index

        
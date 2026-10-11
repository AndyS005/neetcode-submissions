class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        at_index = {}
        for index, value in enumerate(nums):
            temp = target - value
            if temp in at_index:
                return [at_index[temp],index]
            at_index[value] = index



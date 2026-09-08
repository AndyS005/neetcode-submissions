class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        final = []
        for index, value in enumerate(nums):
            difference = target - value
            if difference in mem:
                final = [mem[difference], index]
            mem[value] = index
        return final
        

        
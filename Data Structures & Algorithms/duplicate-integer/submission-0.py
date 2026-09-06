class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = {}
        for i, n in enumerate(nums):
            if nums[i] in history:
                return True
            else:
                history[n] = i
            
        return False

        
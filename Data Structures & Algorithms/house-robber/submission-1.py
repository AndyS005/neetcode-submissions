class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0 
        prev1 = 0 
        new_best = 0 
        for n in nums:
            new_best = max(prev1, n + prev2)
            prev2, prev1 = prev1, new_best
        return prev1
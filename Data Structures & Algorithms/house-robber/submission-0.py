class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        for n in nums:
            new_best = max(n + prev, curr)
            prev = curr
            curr = new_best

        return curr
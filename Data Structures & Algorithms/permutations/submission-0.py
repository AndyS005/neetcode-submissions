class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtrack(path, picked):

            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if picked[i]:
                    continue
                path.append(nums[i])
                picked[i] = True
                backtrack(path, picked)
                path.pop()
                picked[i] = False

            
         
        backtrack([], [False] * len(nums))
        return res
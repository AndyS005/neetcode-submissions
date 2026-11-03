class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
        
            l,r = index + 1, len(nums) - 1

            while l < r:
                total = value + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -=1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l+= 1

        
        return res

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[index] == 0:
                    nums[index] = nums[i]
                    nums[i] = 0 
                index+=1            
            

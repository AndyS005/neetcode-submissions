class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[first]
                nums[first] = nums[i]
                nums[i] = temp
                first+=1                
            

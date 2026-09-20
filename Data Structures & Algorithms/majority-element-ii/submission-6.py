class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        for n in nums:
            if len(nums) < 3:
                res.append(n)
            if n in dic:
                dic[n] += 1
                if dic[n] > len(nums) // 3 and n not in res:
                    res.append(n)
            else:
                dic[n] = 1
        
        
        return res
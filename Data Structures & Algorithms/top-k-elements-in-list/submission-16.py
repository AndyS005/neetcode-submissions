class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        bucket = [[] for i in range(len(nums) + 1)]
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
            
        for num, count in dic.items():
            bucket[count].append(num)

        
        res = []
        for i in range(len(bucket) -1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res






        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        bucket = [[] for i in range(len(nums) + 1)]
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        
        for value, count in dic.items():
            bucket[count].append(value)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for value in bucket[i]:
                res.append(value)
                if len(res) == k:
                    return res
        return res


        
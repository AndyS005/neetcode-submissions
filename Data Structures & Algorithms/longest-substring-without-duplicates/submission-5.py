class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        left = 0 
        total = 0
        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[left])
                left+=1
            subString.add(s[r])
            cur_total = r - left +1
            if cur_total > total:
                total = cur_total
        return total

                

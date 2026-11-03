class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        l = 0 
        total = 0
        for r in s:
            while r in subString:
                subString.remove(s[l])
                l+= 1
            subString.add(r)
            total = max(len(subString), total)
        return total
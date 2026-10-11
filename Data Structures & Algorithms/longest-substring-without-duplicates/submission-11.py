class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        l = 0
        length = 0 
        for r in s:
            while r in subString:
                subString.remove(s[l])
                l+=1
            subString.add(r)
            length = max(length, len(subString))

        return length 

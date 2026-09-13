class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        left = 0 
        length = 0
        for r in s:
            while r in subString:
                subString.remove(s[left])
                left+= 1
            subString.add(r)
            if len(subString) > length:
                length = len(subString)
        return length
        
                

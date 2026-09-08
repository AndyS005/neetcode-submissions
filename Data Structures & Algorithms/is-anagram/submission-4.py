class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}

        for char in s:
            if char not in a:
                a[char] = 1
            else:
                a[char] += 1
           
        for j in t:
            if j not in b:
                b[j] = 1
            else:
                b[j] += 1
        
        if a != b:
            return False
        return True
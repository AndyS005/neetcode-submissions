class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a_count = {}
        b_count = {}
        for i in range(len(s)):
            if s[i] in a_count:
                a_count[s[i]] +=1
            else:
                a_count[s[i]] = 1

        for j in range(len(t)):
            if t[j] in b_count:
                b_count[t[j]] +=1
            else:
                b_count[t[j]] = 1

        if a_count == b_count:
            return True
        return False
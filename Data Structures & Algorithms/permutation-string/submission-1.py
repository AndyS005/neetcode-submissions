class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count_1 = [0] * 26
        count_2 = [0] * 26

        if len(s2) < len(s1):
            return False
        for r in range(len(s1)):
            count_1[ord(s1[r]) - ord("a")] += 1
            count_2[ord(s2[r]) - ord("a")] += 1

        if count_1 == count_2:
            return True

        for i in range(len(s1), len(s2)):
            count_2[ord(s2[i]) - ord("a")] += 1
            count_2[ord(s2[i - len(s1)]) - ord("a")] -=1
            if count_1 == count_2:
                return True
        return False


        
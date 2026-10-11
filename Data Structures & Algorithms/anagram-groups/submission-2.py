class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for word in strs:
            array = [0] * 26 
            for letter in word:
                array[ord("a") - ord(letter)] += 1
            freq[tuple(array)].append(word)
            
        return list(freq.values())



        

        
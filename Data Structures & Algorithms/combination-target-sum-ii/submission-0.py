class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index, path, total):

            if total == target:
                res.append(path[:])
                return
            if total > target:
                return 
            if index == len(candidates):
                return 

                
            path.append(candidates[index])
            backtrack(index + 1, path, total + candidates[index])
            path.pop()

            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1
            backtrack(next_index, path, total)

        backtrack(0, [], 0)
        return res               

        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)
        array = 0
        while l < r:
            curr = l + ((r-l) // 2)
            if matrix[curr][-1] >= target:
                r = curr
            elif matrix[curr][-1] < target:
                l = curr + 1


        if l == len(matrix):
            return False
        
        array = l
        
        first, last = 0, len(matrix[array])
        while first < last:
            curr = first + ((last - first) // 2) #
            if matrix[array][curr] == target:
                return True
            elif matrix[array][curr] < target:
                first = curr + 1
            else:
                last = curr

        return False


        
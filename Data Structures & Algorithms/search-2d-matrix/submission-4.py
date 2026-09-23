class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        array = 0
        while l <= r:
            array = l + ((r-l) // 2)
            if target > matrix[array][-1]:
                l = array + 1
            elif target < matrix[array][0]:
                r = array - 1
            else:
                break
        
        first, last = 0, len(matrix[array]) - 1
        while first <= last:
            curr = first + ((last-first)//2)
            if matrix[array][curr] == target:
                return True
            elif matrix[array][curr] < target:
                first = curr + 1
            else:
                last = curr - 1
        
        return False

        
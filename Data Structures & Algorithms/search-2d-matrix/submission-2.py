class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) - 1
        array = 0 
        while l <= r:
            array = l + ((r - l) // 2)
            if matrix[array][0] == target:
                return True
            elif matrix[array][0] > target:
                r = array - 1
            else:
                first, last = 0, len(matrix[array]) - 1
                while first <= last:
                    curr = first + ((last - first) // 2)
                    if matrix[array][curr] == target:
                        return True
                    elif matrix[array][curr] > target: 
                        last = curr - 1
                    else:
                        first = curr + 1
                l = array + 1
        return False



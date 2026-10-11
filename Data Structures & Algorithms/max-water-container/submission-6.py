class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0    
        left_h, right_h = 0, len(heights) - 1
        for h in heights:
            width = right_h - left_h 
            height = min(heights[right_h], heights[left_h])
            res = max(res, width * height)
            if heights[left_h] > heights[right_h]:
                right_h -= 1
            else:
                left_h += 1
      
    
        return res


        